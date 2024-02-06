# -*- coding: utf-8 -*-
{
    'name': "Landed Cost",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Midaad",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account', 'stock','stock_landed_costs','product','point_of_sale'],
    'data': [
        'views/om_odoo_inheritence_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
