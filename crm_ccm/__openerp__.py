# -*- coding: utf-8 -*-
{
    'name': "CRM and Call Center",

    'summary': """
        CRM and Call Center
        """,

    'description': """
        This module is designed for managing the internal features for iBanh
    """,

    'author': "iBanh",
    'website': "http://www.ibanh.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        #'security/callrecord_security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/config.xml',
        'views/callrecord.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
