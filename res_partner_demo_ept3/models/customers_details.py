from odoo import models, fields


class CustomersDetails(models.Model):
    _name = 'res.partner.demo.ept3'
    _description = 'Partner Demo 3'

    name = fields.Char(string='Name', help='Enter customer Name')
    email = fields.Char(string='Email', help='Enter customer Email')
    street1 = fields.Char(string='Street1', help='Enter customer street address')
    street2 = fields.Char(string='Street2', help='Another line for the street address')
    city = fields.Char(string='City', help='City of the customer')
    state = fields.Char(string='State', help='State where customer lives')
    country = fields.Char(string='Country', help='Country where customer lives')
    zip_code = fields.Char(string='Zipcode', help="Zipcode of the customer's address")
    birthdate = fields.Date(string='Birthdate', help="Birthdate of the customer")
    gender = fields.Selection(string="Gender", help="Gender of the customer", selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    age = fields.Integer(string='Age', help="Age of the customer")
    weight = fields.Float(string="Weight", help="Weight of the customer")
    description = fields.Text(string="Description", help="Description about the customer")
    details = fields.Html(string="Details", help="Details about the customer")
    is_spectacles = fields.Boolean(string="Spectacles", help="Does customer wears spectacles or not")
    photo = fields.Image(string="Photo", help="Photo of the customer")
