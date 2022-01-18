from odoo import fields, models


class Properties(models.Model):
    _name = "estate_property"
    _description = "Real Estate properties"

    title = fields.Char(string='Title', required=True)
    property_type = fields.Char(string='Property Type', required=True)
    post_code = fields.Char(string='Postcode', required=True)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
