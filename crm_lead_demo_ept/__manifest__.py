{
    'name': 'crm.lead.demo.ept',
    'summary': 'CRM Lead Demo Ept',
    'description': """
        Requirement 7
    """,
    'depends': ['base'],
    'data': ['security/crm_lead_security.xml', 'security/ir.model.access.csv', 'views/crm_lead.xml'],
    'demo': ['data/customer_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
