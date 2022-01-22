{
    'name': 'res.partner.demo.ept4',
    'summary': 'Res Partner Demo EPT4',
    'description': """
        Requirement 1
        Module 4
    """,
    'depends': ['sale'],
    'data': ['security/ir.model.access.csv', 'views/customer_details.xml'],
    'demo': ['data/customers_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
