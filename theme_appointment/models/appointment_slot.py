from odoo import fields, models

class AppointmentDetails(models.Model):
    _name = "appointment.slot"
    _description = "Appointment Time Slots"

    staff_id = fields.Many2one('staff.details', strint="Employee name")
    shift_time = fields.Selection([
        ('8 to 16', '8 To 16'),
        ('16 to 23', '16 To 23'),
        ('23 to 8', '23 To 8')
    ], string="Staff type", default="8 to 16")
    start_time = fields.Float(string='Start Date', reqired=True)
    end_time = fields.Float(string='End date', required=True)

    def name_get(self):
        print('------------------->', self)
        result = []
        for doctor in self:
            name = doctor.staff_id
            result.append((doctor.id, name))
        return result



