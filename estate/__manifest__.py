{
    'name': 'estate',
    'summary': 'My Custom Module',
    'description': "",
    'depends': [
        'base_setup',
        'sales_team'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/properties.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
