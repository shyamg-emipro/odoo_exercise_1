{
    'name': 'product.demo.ept',
    'summary': 'Product Demo Ept',
    'description': """
        Requirement 5
    """,
    'depends': ['sales_team'],
    'data': ['security/ir.model.access.csv', 'views/product_details.xml'],
    'demo': ['data/product_data.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}