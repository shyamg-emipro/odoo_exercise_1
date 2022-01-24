{
    'name': 'localization_demo_ept',
    'summary': 'Localization Ept',
    'description': """
        Requirement 2
        Requirement 3
        Requirement 4
     """,
    'depends': ['sales_team'],
    'data': ['security/ir.model.access.csv', 'views/country_details.xml', 'views/state_details.xml', 'views/city_details.xml'],
    'demo': ['data/country_data.xml', 'data/state_data.xml', 'data/city_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
