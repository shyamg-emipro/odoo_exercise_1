from odoo import models, fields


class StateDetails(models.Model):
    _name = 'res.state.demo.ept'
    _description = 'State Demo'

    name = fields.Char(string="Name", help="Name of the state")
    state_code = fields.Char(string="State Code", help="Short code for the state")
    country_name = fields.Char(string="Country Name", help="Country of the State", copy=False)
    active = fields.Boolean(string="Active", help="Whether the state is active or not")
