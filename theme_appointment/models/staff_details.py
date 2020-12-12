from odoo import fields, models

class StaffDetails(models.Model):
    _name = "staff.details"
    _description = "Staff Details"

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Contact", required=True)
    dob = fields.Date(string="Date of Birth", required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default="male")
    job_type = fields.Selection([
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('helper', 'Helper')
    ], string="JOb Type", default="Nurse")
    address = fields.Text(string="Address", required=True)
    qualification = fields.Char(string="Qualification", required=True)
    shift_time = fields.Selection([
        ('8 to 4', '8 To 4'),
        ('4 to 11', '4 To 11'),
        ('11 to 8', '11 To 8')
    ], string="Shift Time", default="8 to 4")
