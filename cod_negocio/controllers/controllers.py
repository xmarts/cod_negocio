# -*- coding: utf-8 -*-
from odoo import http

# class CodNegocio(http.Controller):
#     @http.route('/cod_negocio/cod_negocio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cod_negocio/cod_negocio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cod_negocio.listing', {
#             'root': '/cod_negocio/cod_negocio',
#             'objects': http.request.env['cod_negocio.cod_negocio'].search([]),
#         })

#     @http.route('/cod_negocio/cod_negocio/objects/<model("cod_negocio.cod_negocio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cod_negocio.object', {
#             'object': obj
#         })