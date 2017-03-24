# -*- coding: utf-8 -*

{
    'name': 'Theme: myfactory',
    'version': '1.0.0',
    'summary': '',
    'description': 'Theme for the myfactory project',
    'category': 'Theme',
    'author': 'ohmycode',
    'website': '',
    'license': 'Free',
    'depends': [
        'omc_basic_config',
        'website',
        'website_less',
    ],
    'data': [
        'data/website-menu.xml',
        'data/page-home.xml',
        'data/page-benefits.xml',
        'data/page-packages.xml',
        'data/page-features.xml',

        'views/assets.xml',
        'views/layout.xml',
    ],
    'demo': [''],
    'installable': True,
    'auto_install': False,
}