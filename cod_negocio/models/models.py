# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError


class Cod_vendedor(models.Model):
    _name = "cod.vendedor"
    codigo = fields.Integer(
        string='Código',
    )
    name = fields.Char(string="Nombre")
  


class cod_digo_negicio(models.Model):
    _inherit = 'res.partner'

    tarimas = fields.Selection([
            ('si', 'Si'),
            ('no', 'No'),          
                    
        ], default='si', string="Dejar tarimas")

    flete_externo = fields.Selection([
            ('si', 'Si'),
            ('no', 'No'),          
                    
        ], default='si', string="Flete Externo")

    cod_vendedor = fields.Many2one('cod.vendedor', string="Codigo Vendedor")

    cod_negocio = fields.Selection([
            ('no_definido', 'No definido'),
            ('oxxo', 'Oxxo'),
            ('sams', 'SAMS'),
            ('cuenca', 'Cuenca'),
            ('tiendas_soriana', 'Tiendas Soriana'),
            ('super_bodegas_de_cordoba', 'Super Bodegas de Cordoba'),
            ('wal_mart', 'Wal Mart'),
            ('mexicana_de_abarrotes', 'Mexicana de Abarrotes'),
            ('autoservicios_varios', 'autoservicios_varios'),
            ('super_iberia', 'Super Iberia'),
            ('bodega_aurrera', 'Bodega Aurrera'),
            ('supercito', 'Supercito'),
            ('suma_y_multiplica', 'Suma y Multiplica'),
            ('comercial_mexicana', 'Comercial Mexicana'),
            ('clientes_de_rutas', 'Clientes de Rutas'),
            ('costco_de_mexico', 'Costco de Mexico'),
            ('sahuayo', 'Sahuayo'),
            ('viveres _y_licores', 'Viveres y Licores'),
            ('diconsa', 'Diconsa'),
            ('city_club', 'City Club'),
            ('famacias_guadalajara', 'Famacias Guadalajara'),
            ('super_keyko', 'Super Keyko'),
            ('tiendas_3b', 'Tiendas 3B'),
            ('tiendas_heb', 'Tiendas HEB'),
            ('tiendas_chedraui', 'Tiendas Chedraui'),
            ('super_precio_neto', 'Super Precio /Neto'),
            ('grupo_idea', 'Grupo IDEA'),
            ('fenix', 'Fenix'),
            ('gigante', 'Gigante'),
            ('ayuntamiento', 'Ayuntamiento'),
            ('tamsa', 'Tamsa'),
            ('dif', 'DIF'),
            ('techin', 'Techin'),
            ('sidernet', 'Sidernet'),
            ('x24', 'X24'),
            ('tiendas_imss', 'Tiendas IMSS'),
            ('tiendas_isste', 'Tiendas ISSSTE'),
            ('los_leones', 'Los Leones'),
            ('tiendas_lores', 'Tiendas Lores'),
            ('depositos_jarocho', 'Depositos Jarocho'),
            ('supf', 'Super Fasti'),
            ('bc_comercio', 'Bc Comercio'),
            ('frm_gdl', 'Farm. GDL'),
            ('super_smart', 'Super Smart'),
            ('italian_coffe', 'Italian Coffe'),
        ],  default='no_definido', string="Código Negocio")

    cod_programa = fields.Selection([
            ('depositos', 'Depositos'),
            ('clientes_normales', 'Clientes normales'),
            ('otros', 'Otros'),
           
        ], default='depositos', string="Código Programa")

    cod_zona = fields.Selection([
            ('retiros_depositos', 'Retiros Depositos'),
            ('planta', 'Planta'),
            ('oaxaca', 'Oaxaca'),
            ('otros', 'Otros'),
            ('merida', 'Merida'),
            ('cuenca', 'Cuenca'),
            ('varios', 'Varios'),
            ('cuenca_carlos_najera)', 'Cuenca (Carlos Najera)'),
            ('golfo', 'Golfo'),
            ('centralizados', 'Centralizados'),
            ('aguascalientes', 'Aguascalientes'),
            ('comercializadora BigC', 'Comercializadora BigC'),
            ('puebla', 'Puebla'),
            ('maquila', 'Maquila'),
            ('maquila_comercial_mexicana', 'Maquila Comercial Mexicana'),
            ('maquila_chedraui', 'Maquila Chedraui'),
            ('guadalajara', 'Guadalajara'),
            ('xalapa', 'Xalapa'),
            ('tehuacan', 'Tehuacan'),
            ('tuist', 'Tuist'),
            ('bamba_coco', 'Bamba Coco'),
            ('coatzacoalcos', 'Coatzacoalcos'),
            ('villa_hermosa', 'Villa Hermosa'),
            ('suc_orizaba', 'Suc . Orizaba'),
            ('suc_tuxtepec', 'Suc. Tuxtepec'),
            ('suc_cordoba', 'Suc. Cordoba'),
            ('clientes_varios', 'Clientes Varios'),
            ('zona_sureste', 'Zona Sureste'),
            ('zona_cuenca', 'Zona Cuenca'),
            ('zona_golfo', 'Zona Golfo'),
            ('zona_autoserv_nac', 'Zona Autoserv. Nac.'),
            ('Zona Cuentas Especiales', 'Zona Cuentas Especiales'),
            ('mayoristas_a', 'Mayoristas (A)'),
            ('zona_1_sureste', 'Zona 1 Sureste'),
            ('zona_2_puebla_oaxaca', 'Zona 2 Puebla-Oaxaca'),
            ('zona_3_cuenca', 'Zona 3 Cuenca'),
            ('zona_4_corporativas', 'Zona 4 Corporativas'),
            ('zona_5_cuentas_clave', 'Zona 5 Cuentas Clave'),
            ('chiapas', 'Chiapas'),
            ('mexico', 'México'),
            ('bajio', 'Bajio'),
            ('mov_otras_sucursal', 'Mov. otras sucursal'),           
        ], default='retiros_depositos', string="Código Zona/Ruta")

    ruta_venta = fields.Selection([
            ('acatlan', 'Acatlan'),
            ('oaxaca', 'Oaxaca'),
            ('otros', 'Otros'),
            ('merida', 'Merida'),
            ('cuenca', 'Cuenca'),
            ('varios', 'Varios'),
            ('cuenca_jorge_zamudio)', 'Cuenca (Jorge Zamudio)'),
            ('autoservicios', 'Autoservicios'),
            ('golfo', 'Golfo'),
            ('mayoristas', 'Mayoristas'),
            ('centralizados', 'Centralizados'),
            ('puebla', 'Puebla'),
            ('maquila', 'Maquila'),
            ('tehuacan', 'Tehuacan'),
            ('tuist', 'Tuist'),
            ('bamba_coco', 'Bamba Coco'),
            ('coatzacoalcos', 'Coatzacoalcos'),
            ('villa_hermosa', 'Villa Hermosa'),
            ('clientes_varios', 'Clientes Varios'),
            ('sureste', 'Sureste'),
            ('cuenca', 'Cuenca'),
            ('golfo', 'Golfo'),
            ('autoservicios_nacionales', 'Autoservicios Nacionales'),
            ('cuentas_especiales', 'Cuentas Especiales'),
            ('mayoristas', 'Mayoristas'),
            ('zona_1_sureste', 'Zona 1 Sureste'),
            ('zona_2_puebla_oaxaca', 'Zona 2 Puebla-Oaxaca'),
            ('zona_3_cuenca', 'Zona 3 Cuenca'),
            ('zona_4_corporativas', 'Zona 4 Corporativas'),
            ('zona_cuentas_clave', 'Zona Cuentas Clave'),
            ('chiapas', 'Chiapas'),
            ('mexico', 'Mexico'),
            ('bajio', 'Bajio'),
            ('cobro_x_of_local', 'Cobro X Of. Local'),
            ('cobro_x_of_central', 'Cobro X Of. Central'),            
        ], default='acatlan', string="Ruta Venta")
   

    # cod_de_vendedor = fields.Selection([
    #         ('autoservicion', 'AUTOSERVICIOS'),
    #         ('cuenca', 'CUENCA'),
    #         ('cuenca_1', 'CUENCA 1'),
    #         ('mexico', 'MEXICO'),
    #         ('chiapas', 'CHIAPAS'),
    #         ('merida_villahermoza_coatzacoalcos', 'MERIDA, VILLAHERMOSA Y COATZACOALCOS'),
    #         ('puebla', 'PUEBLA'),
    #         ('salvador_ros', 'SALVADOR ROS'),
    #         ('tampico', 'TAMPICO'),
    #         ('distribuidora_cordoba', 'Distribuidora Cordoba'),
    #         ('distribuidora_orizaba', 'Distribuidora Orizaba'),
    #         ('distribuidora_veracruz', 'Distribuidora Veracruz'),
    #         ('distribuidora_tuxtepec', 'Distribuidora Tuxtepec'),
    #         ('distribuidora_cardel', 'Distribuidora Cardel'),
    #         ('distribuidora_cosamaloapan', 'Distribuidora Cosamaloapan'),
    #         ('distribuidora_tierra_blanca', 'Distribuidora Tierra Blanca'),
    #         ('distribuidora_puebla', 'Distribuidora Puebla'),
    #         ('distribuidora_minatitlan', 'Distribuidora Minatitlan'),
    #         ('distribuidora_xalapa', 'Distribuidora Xalapa'),
    #         ('tampico_1', 'TAMPICO 1'),
    #         ('eduardo_corral', 'Eduardo Corral'),
    #         ('sin_agente', 'Sin Agente'),
    #         ('tehuacan_y_oaxaca', 'TEHUACAN Y OAXACA'),
    #         ('centralizados', 'CENTRALIZADOS'),
    #         ('tuist', 'TUIST'),
    #         ('bamba_coco', 'BAMBA COCO'),
    #         ('juan_roman_rojas', 'Juan Roman Rojas'),
    #         ('mexico', 'MEXICO'),
    #         ('comercial_mexicana', 'Comercial Mexicana'),
    #         ('maquila_chedraui', 'Maquila Chedraui'),
    #         ('maquila', 'MAQUILA'),
    #         ('maquila_2', 'MAQUILA 2'),
    #         ('maquila_1', 'MAQUILA 1'),
                    
    #     ], default='autoservicion', string="Codigo de Vendedor")


    payment_method_id = fields.Many2one(
        'l10n_mx_edi.payment.method',
        string='Forma de pago',
        )


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

    dias_entrega = fields.Integer(
        string='Días de entrega',
    )
    
class campos_facturas(models.Model):
    _inherit = 'account.invoice'
                    

    @api.onchange('partner_id')
    def onchange_partner(self):
        self.l10n_mx_edi_usage = self.partner_id.mx_edi_usage
        self.l10n_mx_edi_payment_method_id = self.partner_id.payment_method_id

    # @api.model
    # def _prepare_refund(self, invoice, date_invoice=None, date=None, description=None, journal_id=None, payment_term_id = None):
    #     """ Prepare the dict of values to create the new credit note from the invoice.
    #         This method may be overridden to implement custom
    #         credit note generation (making sure to call super() to establish
    #         a clean extension chain).

    #         :param record invoice: invoice as credit note
    #         :param string date_invoice: credit note creation date from the wizard
    #         :param integer date: force date from the wizard
    #         :param string description: description of the credit note from the wizard
    #         :param integer journal_id: account.journal from the wizard
    #         :return: dict of value to create() the credit note
    #     """
    #     values = {}
    #     for field in self._get_refund_copy_fields():
    #         if invoice._fields[field].type == 'many2one':
    #             values[field] = invoice[field].id
    #         else:
    #             values[field] = invoice[field] or False

    #     values['invoice_line_ids'] = self._refund_cleanup_lines(invoice.invoice_line_ids)

    #     tax_lines = invoice.tax_line_ids
    #     taxes_to_change = {
    #         line.tax_id.id: line.tax_id.refund_account_id.id
    #         for line in tax_lines.filtered(lambda l: l.tax_id.refund_account_id != l.tax_id.account_id)
    #     }
    #     cleaned_tax_lines = self._refund_cleanup_lines(tax_lines)
    #     values['tax_line_ids'] = self._refund_tax_lines_account_change(cleaned_tax_lines, taxes_to_change)

    #     if journal_id:
    #         journal = self.env['account.journal'].browse(journal_id)
    #     elif invoice['type'] == 'in_invoice':
    #         journal = self.env['account.journal'].search([('type', '=', 'purchase')], limit=1)
    #     else:
    #         journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
    #     values['journal_id'] = journal.id
    #     print("############",payment_term_id)
    #     values['type'] = TYPE2REFUND[invoice['type']]
    #     values['date_invoice'] = date_invoice or fields.Date.context_today(invoice)
    #     values['date_due'] = values['date_invoice']
    #     values['state'] = 'draft'
    #     values['number'] = False
    #     values['origin'] = invoice.number
    #     values['payment_term_id'] = False
    #     values['refund_invoice_id'] = invoice.id

    #     if values['type'] == 'in_refund':
    #         partner_bank_result = self._get_partner_bank_id(values['company_id'])
    #         if partner_bank_result:
    #             values['partner_bank_id'] = partner_bank_result.id

    #     if date:
    #         values['date'] = date
    #     if description:
    #         values['name'] = description
    #     return values

    @api.multi
    @api.returns('self')
    def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
        new_invoices = self.browse()
        for invoice in self:
            # create the new invoice
            values = self._prepare_refund(invoice, date_invoice=date_invoice, date=date,
                                    description=description, journal_id=journal_id)
            print("xxxxxxxxxxxx",invoice.payment_term_id.name)
            refund_invoice = self.create(values)
            if refund_invoice:
                for x in refund_invoice:
                    x.write({'payment_term_id':invoice.payment_term_id.id,'l10n_mx_edi_payment_method_id':invoice.l10n_mx_edi_payment_method_id.id,'l10n_mx_edi_usage':invoice.l10n_mx_edi_usage})
            if invoice.type == 'out_invoice':
                message = _("This customer invoice credit note has been created from: <a href=# data-oe-model=account.invoice data-oe-id=%d>%s</a><br>Reason: %s") % (invoice.id, invoice.number, description)
            else:
                message = _("This vendor bill credit note has been created from: <a href=# data-oe-model=account.invoice data-oe-id=%d>%s</a><br>Reason: %s") % (invoice.id, invoice.number, description)

            refund_invoice.message_post(body=message)
            new_invoices += refund_invoice
        return new_invoices
         


class campos_maniobras(models.Model):
    _inherit = 'sale.order'

    payment_method_id = fields.Many2one(
        'l10n_mx_edi.payment.method',
        string='Forma de pago',
        )


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

    @api.onchange('partner_id')
    def onchange_partner_ids(self):
        self.mx_edi_usage = self.partner_id.mx_edi_usage
        self.payment_method_id = self.partner_id.payment_method_id

    @api.multi
    def _prepare_invoice(self):
        """
        Prepare the dict of values to create the new invoice for a sales order. This method may be
        overridden to implement custom invoice generation (making sure to call super() to establish
        a clean extension chain).
        """
        self.ensure_one()
        company_id = self.company_id.id
        journal_id = (self.env['account.invoice'].with_context(company_id=company_id or self.env.user.company_id.id)
            .default_get(['journal_id'])['journal_id'])
        if not journal_id:
            raise UserError(_('Please define an accounting sales journal for this company.'))
        vinvoice = self.env['account.invoice'].new({'partner_id': self.partner_invoice_id.id})
        # Get partner extra fields
        vinvoice._onchange_partner_id()
        invoice_vals = vinvoice._convert_to_write(vinvoice._cache)
        invoice_vals.update({
            'name': self.client_order_ref or '',
            'origin': self.name,
            'type': 'out_invoice',
            'account_id': self.partner_invoice_id.property_account_receivable_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'journal_id': journal_id,
            'currency_id': self.pricelist_id.currency_id.id,
            'comment': self.note,
            'payment_term_id': self.payment_term_id.id,
            'fiscal_position_id': self.fiscal_position_id.id or self.partner_invoice_id.property_account_position_id.id,
            'company_id': company_id,
            'user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'zona': self.partner_id.zona.id,
            'tipo_cliente':self.partner_id.partner_type_lx,
            'number_store':self.partner_shipping_id.shipping_number_store,
            'l10n_mx_edi_payment_method_id':self.payment_method_id.id,
            'l10n_mx_edi_usage':self.mx_edi_usage,
        })
        return invoice_vals


    tarimas = fields.Selection([('si', 'Si'),('no', 'No')], default='si', string="Dejar tarimas")

    flete_externo = fields.Selection([
            ('si', 'Si'),
            ('no', 'No'),          
                    
        ], default='si', string="Flete Externo")



    pagar = fields.Float(string='Pagar maniobras')
    peso = fields.Float(string="Peso en KG", compute="calcula_peso_total")

    @api.one
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
            

class AccountInvoiceRefund_inherit(models.TransientModel):
    """Credit Notes"""

    _inherit = "account.invoice.refund"
    test = fields.Char(
        string='Filed Label',
    )

    def _get_refund(self, inv, mode):
        self.ensure_one()
        if inv.state in ['draft', 'cancel']:
            raise UserError(_('Cannot create credit note for the draft/cancelled invoice.'))
        if inv.reconciled and mode in ('cancel', 'modify'):
            raise UserError(_(
                'Cannot create a credit note for the invoice which is already reconciled, invoice should be unreconciled first, then only you can add credit note for this invoice.'))

        date = self.date or False
        description = self.description or inv.name
        return inv.refund(self.date_invoice, date, description, inv.journal_id.id)












