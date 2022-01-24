from odoo import models, fields


class CityDetails(models.Model):
    _name = 'res.city.demo.ept'
    _description = 'City Demo'

    name = fields.Char(string="City", help="Name of the city")
    state_name = fields.Char(string="State", help="Name of the state")
    active = fields.Boolean(string="Active", help="Whether the city is active or not")
