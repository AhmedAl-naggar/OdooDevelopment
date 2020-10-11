# -*- coding: utf-8 -*-
{
    'name': "Al-naggar Net",

    'summary': """
        Al-naggar Net App used to manage internet network resources.
        * Clients
        * Sales
        * Purchases 
        """,

    'description': """
        Al-naggar Net App used to manage internet network resources:
    """,

    'author': "Ahmed S. Al-naggar",
    'website': "http://www.alnaggar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/templates.xml',
        'views/alnaggarnet.xml',
        'views/partner.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
