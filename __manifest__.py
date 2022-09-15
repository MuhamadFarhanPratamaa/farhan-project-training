# -*- coding: utf-8 -*-
{
    'name': "farhanfutsal",

    'summary': """
        odoo module for farhan lapangan futsal""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/lapangan_view.xml',
        'views/sewalapangan_view.xml',
        'views/pelanggan_view.xml',
        'views/pembayaran_view.xml',
        'report/report.xml',
        'report/print_faktur_pembayaran.xml',
        'wizzard/addlapangan_wizzard_view.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
