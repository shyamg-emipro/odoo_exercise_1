from odoo import models, fields


class CrmLead(models.Model):
    _name = 'crm.lead.demo.ept'
    _description = 'CRM Lead'

    name = fields.Char(string="Name", help="Name of the customer", requrired=True)
    email = fields.Char(string="Email", help="Email of the customer", requrired=True)
    phone = fields.Char(string="Phone", help="Phone number of the customer", requrired=True)
    expected_revenue = fields.Float(string="Expected Revenue", help="Expected Revenue from the customer", digits=(10, 2))
    salesperson = fields.Char(string="Salesperson", help="Salesperson", required=True)
    sales_team = fields.Char(string="Sales Team", help="Sales Team")
    campaign = fields.Char(string="Campaign", help="Campaign")
    channel = fields.Selection(string="Channel",
                               help="Channel",
                               selection=[('Facebook', 'Facebook'),
                                          ('WhatsApp', 'WhatsApp'),
                                          ('Email', 'Email'),
                                          ('Newspaper', 'Newspaper'),
                                          ('Television', 'Television'),
                                          ('Phone', 'Phone'),
                                          ('Call', 'Call'),
                                          ('SMS', 'SMS'),
                                          ('Google Ads', 'Google Ads')],
                               required=True)
    state = fields.Selection(string="State",
                             help="State of the lead",
                             selection=[('New', 'New'),
                                        ('Qualified', 'Qualified'),
                                        ('Proposition', 'Proposition'),
                                        ('Won', 'Won'),
                                        ('Lost', 'Lost')],
                             default="New")
    follow_up_date = fields.Date(string="Follow Up Date", help="Follow Up Date", required=True)
    won_date = fields.Date(string="Won Date", help="Won date")
    lost_reason = fields.Text(string="Lost Reason", help="Reason why order is lost")

