{
    'name': 'Purchase & Sales Connector',
    'version': '1.0.0',
    'category': 'Tools',
    'summary': 'Connect Purchase and Sales Modules',
    'description': """
        Purchase & Sales Connector for Odoo
    """,
    'author': 'Yusuf',
    'website': 'https://github.com/Yusufislam-id/custom_yusuf',
    'license': 'LGPL-3',
    'depends': ['sale', 'purchase',],
    'data': [
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}