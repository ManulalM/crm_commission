{
    'name': 'crm_commission',
    'version': '16.0.1.0.0',
    'summary': 'crm commission System',
    'sequence': 10,
    'description': """
Crm Commission System
====================
This is a system that explains the complete working of commission management.
    """,
    'category': 'services',
    'depends': ['contacts', 'base', 'sale_management', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_commission.xml',
        'views/sales_cm.xml',
        'views/sales_person.xml',
        'views/sales_team.xml',
        'views/menuitems.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': True,
    'license': 'LGPL-3'
}
