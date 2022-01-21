{
    'name': 'res.partner.demo.ept2',
    'summary': 'Res Partner Demo EPT2',
    'description': """
        Requirement 1
        Module 2
    """,
    'depends': ['sale'],
    'data': ['security/ir.model.access.csv', 'views/customer_details.xml', 'data/customers_data.xml'],
    'demo': ['data/customers_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
