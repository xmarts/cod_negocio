# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp


class ProductProduct(models.Model):
    _inherit = "product.product"

    standard_price = fields.Float(
        'Cost',
        company_dependent=True,
        digits=dp.get_precision('Product Price'),
        groups="base.group_user",
        store=True,
        help="Cost used for stock valuation in standard price and as a first price to set in average/fifo. "
               "Also used as a base price for pricelists. "
               "Expressed in the default unit of measure of the product.")
    standard_price_rel = fields.Float(
        'Coste',
        related="standard_price",
        store=True,
        digits=dp.get_precision('Product Price'))
