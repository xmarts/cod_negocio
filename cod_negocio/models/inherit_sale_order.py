# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one(
        'l10n_mx_edi.payment.method',
        string='Forma de pago')
    mx_edi_usage = fields.Selection([
        ('G01', 'Acquisition of merchandise'),
        ('G02', 'Returns, discounts or bonuses'),
        ('G03', 'General expenses'),
        ('I01', 'Constructions'),
        ('I02', 'Office furniture and equipment investment'),
        ('I03', 'Transportation equipment'),
        ('I04', 'Computer equipment and accessories'),
        ('I05', 'Dices, dies, molds, matrices and tooling'),
        ('I06', 'Telephone communications'),
        ('I07', 'Satellite communications'),
        ('I08', 'Other machinery and equipment'),
        ('D01', 'Medical, dental and hospital expenses.'),
        ('D02', 'Medical expenses for disability'),
        ('D03', 'Funeral expenses'),
        ('D04', 'Donations'),
        ('D05', 'Real interest effectively paid for mortgage loans (room house)'),
        ('D06', 'Voluntary contributions to SAR'),
        ('D07', 'Medical insurance premiums'),
        ('D08', 'Mandatory School Transportation Expenses'),
        ('D09', 'Deposits in savings accounts, premiums based on pension plans.'),
        ('D10', 'Payments for educational services (Colegiatura)'),
        ('P01', 'To define'),
    ], 'Usage', default='P01',
        help='Used in CFDI 3.3 to express the key to the usage that will '
        'gives the receiver to this invoice. This value is defined by the '
        'customer. \nNote: It is not cause for cancellation if the key set is '
        'not the usage that will give the receiver of the document.')
    tarimas = fields.Selection([
        ('si', 'Si'),
        ('no', 'No')
    ], default='si', string="Dejar tarimas")
    flete_externo = fields.Selection([
        ('si', 'Si'),
        ('no', 'No'),
    ], default='si', string="Flete Externo")
    pagar = fields.Float(string='Pagar maniobras')
    peso = fields.Float(string="Peso en KG", compute="calcula_peso_total")

    @api.onchange('partner_id')
    def onchange_partner_ids(self):
        self.mx_edi_usage = self.partner_id.mx_edi_usage
        self.payment_method_id = self.partner_id.payment_method_id

    # @api.multi
    # def _prepare_invoice(self):
    #     """
    #     Prepare the dict of values to create the new invoice for a sales order. This method may be
    #     overridden to implement custom invoice generation (making sure to call super() to establish
    #     a clean extension chain).
    #     """
    #     self.ensure_one()
    #     company_id = self.company_id.id
    #     journal_id = (self.env['account.invoice'].with_context(company_id=company_id or self.env.user.company_id.id)
    #         .default_get(['journal_id'])['journal_id'])
    #     if not journal_id:
    #         raise UserError(_('Please define an accounting sales journal for this company.'))
    #     vinvoice = self.env['account.invoice'].new({'partner_id': self.partner_invoice_id.id})
    #     # Get partner extra fields
    #     vinvoice._onchange_partner_id()
    #     invoice_vals = vinvoice._convert_to_write(vinvoice._cache)
    #     invoice_vals.update({
    #         'name': self.client_order_ref or '',
    #         'origin': self.name,
    #         'type': 'out_invoice',
    #         'account_id': self.partner_invoice_id.property_account_receivable_id.id,
    #         'partner_shipping_id': self.partner_shipping_id.id,
    #         'journal_id': journal_id,
    #         'currency_id': self.pricelist_id.currency_id.id,
    #         'comment': self.note,
    #         'payment_term_id': self.payment_term_id.id,
    #         'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
    #         'company_id': company_id,
    #         'user_id': self.user_id and self.user_id.id,
    #         'team_id': self.team_id.id,
    #         'transaction_ids': [(6, 0, self.transaction_ids.ids)],
    #         'zona': self.partner_id.zona.id,
    #         'tipo_cliente':self.partner_id.partner_type_lx,
    #         'number_store':self.partner_shipping_id.shipping_number_store,
    #         'l10n_mx_edi_payment_method_id':self.payment_method_id.id,
    #         'l10n_mx_edi_usage':self.mx_edi_usage,
    #     })
    #     return invoice_vals

    def _prepare_invoice(self):  # FIXME: Revisar esta parte
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(_('Please define an accounting sales journal for the company %s (%s).', self.company_id.name, self.company_id.id))
        invoice_vals = {
            'ref': self.client_order_ref or '',
            'move_type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'user_id': self.user_id.id,
            'invoice_user_id': self.user_id.id,
            'team_id': self.team_id.id,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
            'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals

    # @api.one
    @api.depends('order_line')
    def calcula_peso_total(self):
        if not self.order_line:
            self.peso = 0
        else:
            for x in self.order_line:
                self.peso += x.product_id.weight *x.product_uom.factor_inv* x.product_uom_qty

    @api.onchange('partner_id')
    def _onchange_partner_id_mani(self):
        self.tarimas = self.partner_id.tarimas
        self.flete_externo = self.partner_id.flete_externo
