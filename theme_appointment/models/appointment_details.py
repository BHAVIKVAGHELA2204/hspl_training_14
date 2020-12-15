from odoo import fields, models

class AppointmentDetails(models.Model):
    _name = "appointment.details"
    _description = "Appointment Information"
    _rec_name = "doctor_name"

    f_name = fields.Char(string='First Name', required=True)
    l_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Contact', required=True)
    date = fields.Date(string='Appointment Date', required=True)
    message = fields.Text(string='Message', required=True)
    doctor_name = fields.Many2one('staff.details', string="Doctor")


