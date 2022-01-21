from odoo import models, fields


class PartnerDemo1(models.Model):
    _name = "res.partner.demo.ept1"
    _description = "Partner Demo 1"

    name = fields.Char(string="Name", help="Name of the partner")
    email = fields.Char(string="Email", help="Email address of the partner")
    street1 = fields.Char(string="Street1", help="Street address of the partner")
    street2 = fields.Char(string="Street2", help="Another line for the Street Address")
    state = fields.Char(string="State", help="State of the partner")
    city = fields.Char(string="City", help="City of the partner")
    zip_code = fields.Char(string="Zipcode", help="Zipcode of the partner's address")
    country = fields.Char(string="Country", help="Country where partner lives in")
    birthdate = fields.Date(string="Date", help="Partner's Birthdate")
    age = fields.Integer(string="Age", help="Partner's Age")
    weight = fields.Float(string="Weight", help="Partner's Weight")
    description = fields.Text(string="Description", help="Description about the partner")
    gender = fields.Selection(string="Gender", help="Partner's Gender", selection=[('Male', 'Male'),('Female', 'Female'),('Other', 'Other')])
    details = fields.Html(string="Details", help="Details about the partner")
    is_spectacles = fields.Boolean(string="Have Spectacles", help="Specified")
    photo = fields.Image(string="Photo", help="Photo of the partner")
