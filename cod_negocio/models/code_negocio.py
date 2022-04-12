# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CodNegocio(models.Model):
    _name = 'code.negocio'

    code = fields.Char(string="Codigo")
    name = fields.Char(string="Nombre")
