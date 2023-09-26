# -*- coding: utf-8 -*-

{
    'name': 'Product Image in Manufacturing Order',
    'version': '1.0',
    'author': 'Craftsync Technologies',
    'maintainer': 'Craftsync Technologies',
    'summary': "Find product's image in manufacturing line.",
    'description': """
Product image in manufacturing order:
=====================
You can see product image in manufacturing order report and manufacturing order as well as.""",
    'website': 'https://www.craftsync.com',
    'category': 'Sales',
    'depends': ['mrp'],
    'data': [
        
        'views/manufacturing.xml',
        'views/report.xml',

    ],
    'license': 'OPL-1',
    'support':'info@craftsync.com',
    'demo': [],
    'images': ['static/description/main_screen.png'],
    'price': 3.99,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
}
