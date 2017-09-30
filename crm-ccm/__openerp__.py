# -*- coding: utf-8 -*-
{
    'name': "crm-ccm",

    'summary': """
        CRM and CCM
        """,

    'description': """
        This module is designed for analyzing customer relationship
    """,

    'author': "iBanh JSC",
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
        # 'security/ir.model.access.csv',
        'views/menus.xml',
        'views/calltype.xml',
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
