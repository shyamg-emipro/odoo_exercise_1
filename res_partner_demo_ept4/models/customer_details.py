from odoo import models, fields


class CustomerDetails(models.Model):
    _name = "res.partner.demo.ept4"
    _description = "Partner Demo 4"

    name = fields.Char(string="Name", help="Name of the customer")
    email = fields.Char(string="Email", help="Email id of the customer")
    street1 = fields.Char(string="Street1", help="Address of the customer")
    street2 = fields.Char(string="Street2", help="Another address line")
    city = fields.Char(string="City", help="City where customer lives")
    state = fields.Char(string="State", help="State where customer lives")
    country = fields.Char(string="Country", help="Country where customer lives")
    zip_code = fields.Char(string="Zipcode", help="Zipcode of the customer's address")
    birthdate = fields.Date(string="Birthdate", help="Birthdate of the customer")
    age = fields.Integer(string="Age", help="Age of the customer")
    weight = fields.Float(string="Weight", help="Weight of the customer")
    gender = fields.Selection(string="Gender", help="Gender of the customer", selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    description = fields.Text(string="Description", help="Description about the customer")
    details = fields.Html(string="Details", help="Details about the customer")
    is_spectacles = fields.Boolean(string="Spectacles", help="Does customer wears spectacles or not")
    photo = fields.Image(string="Photo", help="Photo of the customer")
    
