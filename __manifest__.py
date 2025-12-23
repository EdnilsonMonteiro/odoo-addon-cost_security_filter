{
    'name': 'Filtro de Segurança de Custo (Popup)',
    'version': '1.1',
    'category': 'Inventory',
    'license': 'LGPL-3',
    'depends': ['purchase', 'stock', 'stock_account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/cost_confirmation_wizard_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}