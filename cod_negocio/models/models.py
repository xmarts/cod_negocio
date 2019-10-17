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
        ], default='retiros_depositos', string="Código zona")

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
   

    cod_de_vendedor = fields.Selection([
            ('autoservicion', 'AUTOSERVICIOS'),
            ('cuenca', 'CUENCA'),
            ('cuenca_1', 'CUENCA 1'),
            ('mexico', 'MEXICO'),
            ('chiapas', 'CHIAPAS'),
            ('merida_villahermoza_coatzacoalcos', 'MERIDA, VILLAHERMOSA Y COATZACOALCOS'),
            ('puebla', 'PUEBLA'),
            ('salvador_ros', 'SALVADOR ROS'),
            ('tampico', 'TAMPICO'),
            ('distribuidora_cordoba', 'Distribuidora Cordoba'),
            ('distribuidora_orizaba', 'Distribuidora Orizaba'),
            ('distribuidora_veracruz', 'Distribuidora Veracruz'),
            ('distribuidora_tuxtepec', 'Distribuidora Tuxtepec'),
            ('distribuidora_cardel', 'Distribuidora Cardel'),
            ('distribuidora_cosamaloapan', 'Distribuidora Cosamaloapan'),
            ('distribuidora_tierra_blanca', 'Distribuidora Tierra Blanca'),
            ('distribuidora_puebla', 'Distribuidora Puebla'),
            ('distribuidora_minatitlan', 'Distribuidora Minatitlan'),
            ('distribuidora_xalapa', 'Distribuidora Xalapa'),
            ('tampico_1', 'TAMPICO 1'),
            ('eduardo_corral', 'Eduardo Corral'),
            ('sin_agente', 'Sin Agente'),
            ('tehuacan_y_oaxaca', 'TEHUACAN Y OAXACA'),
            ('centralizados', 'CENTRALIZADOS'),
            ('tuist', 'TUIST'),
            ('bamba_coco', 'BAMBA COCO'),
            ('juan_roman_rojas', 'Juan Roman Rojas'),
            ('mexico', 'MEXICO'),
            ('comercial_mexicana', 'Comercial Mexicana'),
            ('maquila_chedraui', 'Maquila Chedraui'),
            ('maquila', 'MAQUILA'),
            ('maquila_2', 'MAQUILA 2'),
            ('maquila_1', 'MAQUILA 1'),
                    
        ], default='autoservicion', string="Codigo de Vendedor")


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



    tarimas = fields.Selection([
            ('si', 'Si'),
            ('no', 'No'),          
                    
        ], default='si', string="Dejar tarimas")

    flete_externo = fields.Selection([
            ('si', 'Si'),
            ('no', 'No'),          
                    
        ], default='si', string="Flete externo")

    pagar = fields.Float(
        string='Pagar maniobras',
    )




class campos_facturas(models.Model):
    _inherit = 'account.invoice'
                    

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        self.l10n_mx_edi_usage = self.partner_id.mx_edi_usage
        self.l10n_mx_edi_payment_method_id = self.partner_id.payment_method_id        














