# -*- coding: utf-8 -*-
{
    'name': "Delivery Address",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','account', 'sale','l10n_ve_formato_factura_nd_nc','stock','sale_stock'],

    'data': [
        'security/ir.model.access.csv',
        'report/paperformat.xml',
        'report/ir_action_report.xml',
        'views/delivery_sicn.xml',
        'views/delivery_route.xml',
        'views/delivery_partner.xml',
        'views/delivery_sale.xml',
        'views/delivery_account.xml',
        'views/report_savia.xml',
    ],

    'demo': [
        # 'demo/demo.xml',
    ],
}
