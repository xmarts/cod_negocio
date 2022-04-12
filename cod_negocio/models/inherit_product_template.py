# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.addons import decimal_precision as dp


class ProductTemplate(models.Model):
    _inherit = "product.template"

    standard_price = fields.Float(
        'Cost',
        compute='_compute_standard_price',
        inverse='_set_standard_price',
        search='_search_standard_price',
        digits=dp.get_precision('Product Price'),
        groups="base.group_user",
        store=True,
        help="Cost used for stock valuation in standard price and as a first price to set in average/FIFO.")
    standard_price_rel = fields.Float(
        'Coste',
        related="standard_price",
        store=True,
        digits=dp.get_precision('Product Price'))
