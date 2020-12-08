from odoo import http

class CuetomAppointment(http.Controller):
    @http.route('/appointment', auth='public', type='http', website=True)
    def appointment_page(self,  **kwargs):
        return http.request.render('theme_appointment.appointment_page')



