from odoo import http
from odoo.http import request

class CuetomAppointment(http.Controller):
    @http.route('/appointment', auth='public', type='http', website=True)
    def appointment_page(self,  **kwargs):
        doctor_rec = request.env['staff.details'].sudo().search([('job_type', '=', 'doctor')])
        slot_rec = request.env['appointment.slot'].sudo().search([])
        print('------------------------->', slot_rec)
        return http.request.render('theme_appointment.appointment_page', {'doctor_rec': doctor_rec, 'slot_rec': slot_rec})

    # @http.route('/contactus-thank-you', auth='public', type='http', website=True)
    # def contactus_thanks(self, **kwargs):
    #     return http.request.render('website_form.contactus_thanks')

    @http.route('/patient', auth='public', type='http', website=True)
    def patient_page(self, **kwargs):
        return http.request.render('theme_appointment.patient_page')


    @http.route('/add_patient', auth='public', type='http', website=True)
    def add_doc_patient(self, **kw):
        print("-------------------------------------------->")
        request.evn['patient.details'].sudo().create(kw)
        return request.render('theme_appointment.contactus_thanks', {})


    # @http.route('/Appointment_form', auth='public', type='http', website=True)
    # def create_appointment(self, **kwargs):
    #     return request.render('website_form.contactus_thanks', {})

    # @http.route('/website_form', type='http', auth="public", methods=['POST'], website=True, csrf=True)
    # def check_form(self, **post):
    #     # ...
    #     return http.request.render('/contactus-thank-you')

    # @http.route('/website_form', type='http', methods=['POST'], auth="public", website=True, csrf=False)
    # def test_path(self, **kw):
    #     # here in kw you can get the inputted value
    #     print('------------------------->', kw['f_name'])

    # @http.route('/appointment_form', type='http', methods=['POST'], auth="public", website=True, csrf=False)
    # def test_path(self, **kwargs):
    #     # here in kw you can get the inputted value
    #     request_env = request.env['marketplace.request.seller'].sudo()
    #     request_env.sudo().create(kwargs)






