from odoo import models, fields


class EmployeeDetails(models.Model):
    _name = "employee.demo.ept"
    _description = "Employee Demo"

    name = fields.Char(string="Name", help="Name of the employee")
    department = fields.Char(string="Department", help="Department of the employee")
    job_position = fields.Char(string="Position", help="Job Position of the employee")
    salary = fields.Float(string="Salary", help="Salary of the employee", digits=(6, 2))
    hire_date = fields.Date(string="Joining Date", help="Joining Date of the employee")
    gender = fields.Selection(string="Gender",
                              help="Gender of the Employee",
                              selection=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')])
    job_type = fields.Selection(string="Job Type",
                                help="Job Type of the Employee",
                                selection=[('Permanent', 'Permanent'), ('Ad Hoc', 'Ad Hoc')])
