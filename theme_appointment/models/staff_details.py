from odoo import fields, models

class StaffDetails(models.Model):
    _name = "staff.details"
    _description = "Staff Details"

    f_name = fields.Char(string="First Name", required=True)
    l_name = fields.Char(string="Last Name", required=True)
    email = fields.Char(string="Email", required=True)
    phone = fields.Char(string="Contact", required=True)
    dob = fields.Date(string="Date of Birth", required=True)
    profile = fields.Binary(string="Profile Image", help="This field holds the image used as avatar for \
        this contact, limited to 1024x1024px")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default="male")
    job_type = fields.Selection([
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('helper', 'Helper')
    ], string="JOb Type", default="nurse")
    address = fields.Text(string="Address", required=True)
    qualification = fields.Char(string="Qualification", required=True)