{
    'name': 'Herança de Views para Fundações',
    'version': '16.0.1.0.0',
    'summary': 'Manages foundations, machines, services, and measurements.',
    'sequence': 11,
    'description': """Long defsfsdfsd scription""",
    'author': 'Brainess Company, Odoo Community Association (OCA)',
    'category': 'Construction',
    'website': 'https://www.brainesscompany.com',
    'images': [],
    'depends': [
        'base',
        'sale',
        'account',
        'foundation_management',
    ],
    'data': [
        'views/account_invoice_view_inherit.xml',
        'views/sale_order_view_inherit.xml',
    ],

    'demo': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
