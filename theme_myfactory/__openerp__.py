# -*- coding: utf-8 -*

{
    'name': 'Theme: myfactory',
    'version': '1.0.0',
    'summary': '',
    'description': 'Theme for the myfactory project',
    'category': 'Theme',
    'author': 'ohmycode',
    'website': '',
    'depends': [
        'omc_basic_config',
        'website',
        'website_less',
        'website_crm',
        'product',
    ],
    'data': [
        'data/website-menu.xml',
        'data/website-footer.xml',
        'data/website-footer-copyright.xml',
        'data/page-home.xml',
        'data/page-benefits.xml',
        'data/page-packages.xml',
        'data/page-features.xml',
        'data/page-about-us.xml',
        'data/page-demo.xml',
        'data/page-contact-us.xml',
        'data/page-contact-us-thank-you.xml',
        'data/page-ask-for-trial.xml',

        'views/assets.xml',
        'views/layout.xml',

        'views/crm_lead_line_view.xml',
        'views/crm_lead_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
