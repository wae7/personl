# -*- coding: utf-8 -*-
{
    'name': "translate",
    'sequence': -90,
    "author": "Midaad Company",
    'website': "https://midaad.com/",

    'summary': """
        """,
    'description': """
        Long description of module's purpose
    """,

    'category': 'Uncategorized',
    'version': '0.1',
    'depends':  ['base', 'account', 'mrp', 'crm','sale','product','stock'],
    'data': [
        "views/sale_order_line_view.xml",
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'auto_install': False,
    'licence':'LGPL_3',
}
