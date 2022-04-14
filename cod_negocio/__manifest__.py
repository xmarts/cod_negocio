# -*- coding: utf-8 -*-
{
    'name': "cod_negocio",
    'summary': """Agrega campos a los contactos""",
    'description': """Long description of module's purpose""",
    'author': "Xmarts",
    'contributors': "daviddiaz@xmarts.com, javier.hilario@xmarts.com",
    'website': "http://www.xmarts.com",
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base', 'account', 'sale', 'l10n_mx_edi_extended'],
    'data': [
        'security/ir.model.access.csv',
        'views/code_negocio_views.xml',
        'views/inherit_res_partner_views.xml',
        'views/inherit_sale_order_views.xml',
        'report/sale_report_templates.xml',
    ]
}
