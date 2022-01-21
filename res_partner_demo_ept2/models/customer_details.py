from odoo import models, fields


class CustomerDetails2(models.Model):
    _name = "res.partner.demo.ept2"
    _description = "Partner Demo 2"

    name = fields.Char(string="Name", help="Name of the customer")
    email = fields.Char(string="Email", help="Email Address of the Customer")
    street1 = fields.Char(string="Street1", help="Street Address of the customer")
    street2 = fields.Char(string="Street2", help="Another line of the street address")
    city = fields.Char(string="City", help="City where customer lives")
    state = fields.Char(string="State", help="State of the customer address")
    zip_code = fields.Char(string="Zipcode", help="Zipcode of the customer address")
    country = fields.Char(string="Country", help="Country where customer lives")
    birthdate = fields.Date(string="Birthdate", help="Birthdate of the customer")
    age = fields.Integer(string="Age", help="Age of the customer")
    weight = fields.Float(string="Weight", help="Weight of the customer")
    description = fields.Text(string="Description", help="Description about the customer")
    gender = fields.Selection(string="Gender", help="Gender of the customer", selection=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    details = fields.Html(string="Details", help="Details about the customer")
    is_spectacles = fields.Boolean(string="Spectacles", help="Does customer wears the spectacles")
    photo = fields.Image(string="Photo", help="Image of the customer")
