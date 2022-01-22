{
    'name': 'res.partner.demo.ept3',
    'summary': 'Res Partner Demo EPT3',
    'description': """
        Requirement 1
        Module 3
    """,
    'depends': ['sale'],
    'data': ['security/ir.model.access.csv', 'views/customers_details.xml'],
    'demo': ['data/customers_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
