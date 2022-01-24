from odoo import models, fields


class CountriesDetails(models.Model):
    _name = 'res.country.demo.ept'
    _description = 'Country Demo'

    country_name = fields.Char(string="Name", help="Name of the country")
    country_code = fields.Char(string="Code", help="Country Code")
    active = fields.Boolean(string="Active", help="Whether the record is active or not")
    