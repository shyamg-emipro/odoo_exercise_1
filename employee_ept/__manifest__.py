{
    'name': 'employee_ept',
    'summary': 'Employee Ept',
    'description': """
        Requirement 6
    """,
    'depends': ['sales_team'],
    'data': ['security/ir.model.access.csv', 'views/employee_details.xml'],
    'demo': ['data/employee_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
