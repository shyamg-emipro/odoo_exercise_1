from odoo import fields, models


class Properties(models.Model):
    _name = "estate.property"
    _description = "Real Estate properties"

    title = fields.Char(string='Title', required=True)
    owner = fields.Char(string='Owner Name', required=True)
    owner_gender = fields.Selection(string='Gender', required=True, selection=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    property_type = fields.Char(string='Property Type', required=True)
    post_code = fields.Char(string='Postcode', required=True)
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
