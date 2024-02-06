# -*- coding: utf-8 -*-
{
    'name': "Advance",

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
    'depends': ['base', 'account', 'mrp', 'crm','sale','product','stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/om_odoo_inheritence_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
