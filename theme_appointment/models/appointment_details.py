from odoo import fields, models, api, _
from odoo.exceptions import UserError
from odoo.http import request



class AppointmentDetails(models.Model):
    _name = "appointment.details"
    _description = "Appointment Information"

    f_name = fields.Char(string='First Name')
    l_name = fields.Char(string='Last Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Contact')
    date = fields.Date(string='Appointment Date')
    message = fields.Text(string='Message')
    app_slot_id = fields.Many2one('appointment.slot', string="Appointment Slot")
    staff_id = fields.Many2one('staff.details', string="Doctor")

    @api.model
    def create(self, values):
        doctor = values.get("staff_id")
        date = values.get("date")
        slot = values.get("app_slot_id")
        appointment_details_len = self.env['appointment.details'].search_count(
            [('date', '=', date), ('app_slot_id', '=', slot), ('staff_id', '=', doctor)])
        # appointment_details_len = self.env['appointment.details'].search(
        #     [('date', '=', date), ('app_slot_id', '=', slot)])
        # test = len(appointment_details_len)

        if appointment_details_len >= 4:
            # print('---------------->', appointment_details_len, type(appointment_details_len))
            raise UserError(_('Slot already reserved'))
        res = super(AppointmentDetails, self).create(values)
        return res

        @api.onchange('sale_delivery_settings')
        def _onchange_sale_delivery_settings(self):


        # for appointment_details_id in appointment_details_ids:
        #     test = appointment_details_id
        #     # test = str(appointment_details_id.shift_time) + '( ' + str(appointment_details_id.start_time) + ' To ' + str(appointment_details_id.end_time) + ' )'
        #     print('-------------------->', test, date, slot)

        # date = values.get("date")
        # slot = values.get("app_slot_id")
        # self
        # print('----------------->', self, values)

    # @api.model
    # def create(self, vals):
    #     print("-----> :", vals)
    #     vals.update({"name" : vals.get("f_name")+" 123"})
    #     # print("new val: ", vals)
    #     res = super(Student, self).create(vals)
    #     # print("val 1 : ", res)
    #     # print("value", res.roll_no, "Name :" + res.name + " vaghela")
    #     return res
