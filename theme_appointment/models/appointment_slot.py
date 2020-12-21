from odoo import fields, models

class AppointmentDetails(models.Model):
    _name = "appointment.slot"
    _description = "Appointment Time Slots"
    _rec_name = "shift_time"

    staff_id = fields.Many2one('staff.details', strint="Staff")
    shift_time = fields.Selection([
        ('morning', 'Morning'),
        ('noon', 'Noon'),
        ('Evening', 'Evening')
    ], string="Staff type", default="morning")
    start_time = fields.Float(string='From Time')
    end_time = fields.Float(string='To Time')

    def name_get(self):
        result = []
        for doctor in self:
            name = doctor.shift_time + '( ' + str(doctor.start_time) + ' To ' + str(doctor.end_time) + ' )'
            result.append((doctor.id, name))
        return result





