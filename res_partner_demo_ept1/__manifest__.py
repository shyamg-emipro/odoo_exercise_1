{
    'name': 'res_partner_demo_ept1',
    'summary': 'Res Partner Demo EPT1',
    'description': """
        Requirement 1: First Model,
        This models is created for the learning purposes.
    """,
    'depends': ['sale'],
    'data': ['security/ir.model.access.csv', 'views/partner_details.xml', 'data/customers_records.xml'],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False

}
