# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cod_digo_negicio(models.Model):
    _inherit = 'res.partner'

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
        ],  default='no_definido', string="Codigo Negocio")

    cod_programa = fields.Selection([
            ('depositos', 'Depositos'),
            ('clientes_normales', 'Clientes normales'),
            ('otros', 'Otros'),
           
        ], default='depositos', string="Codigo Programa")
























