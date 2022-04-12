# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


# class AccountInvoiceRefund_inherit(models.TransientModel):
#     """Credit Notes"""

#     _inherit = "account.invoice.refund"
#     test = fields.Char(
#         string='Filed Label',
#     )

#     def _get_refund(self, inv, mode):
#         self.ensure_one()
#         if inv.state in ['draft', 'cancel']:
#             raise UserError(_('Cannot create credit note for the draft/cancelled invoice.'))
#         if inv.reconciled and mode in ('cancel', 'modify'):
#             raise UserError(_(
#                 'Cannot create a credit note for the invoice which is already reconciled, invoice should be unreconciled first, then only you can add credit note for this invoice.'))

#         date = self.date or False
#         description = self.description or inv.name
#         return inv.refund(self.date_invoice, date, description, inv.journal_id.id)
