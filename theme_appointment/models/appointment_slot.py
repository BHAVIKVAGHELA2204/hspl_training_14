from odoo import fields, models

class AppointmentDetails(models.Model):
    _name = "appointment.slot"
    _description = "Appointment Time Slots"

    staff_id = fields.Char('')
