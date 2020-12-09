from odoo import http

class CuetomAppointment(http.Controller):
    @http.route('/appointment', auth='public', type='http', website=True)
    def appointment_page(self,  **kwargs):
        return http.request.render('theme_appointment.appointment_page')

    # @http.route('/website_form', type='http', methods=['POST'], auth="public", website=True, csrf=False)
    # def test_path(self, **kw):
    #     # here in kw you can get the inputted value
    #     print('------------------------->', kw['f_name'])

    # @http.route('/appointment_form', type='http', methods=['POST'], auth="public", website=True, csrf=False)
    # def test_path(self, **kwargs):
    #     # here in kw you can get the inputted value
    #     request_env = request.env['marketplace.request.seller'].sudo()
    #     request_env.sudo().create(kwargs)






