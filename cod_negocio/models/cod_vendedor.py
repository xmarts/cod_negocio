# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CodVendedor(models.Model):
    _name = "cod.vendedor"
    _description = "cod.vendedor"

    codigo = fields.Integer(string='Código')
    name = fields.Char(string="Nombre")
