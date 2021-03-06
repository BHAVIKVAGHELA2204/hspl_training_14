{
    'name': 'Theme Appointment',
    'description': 'A Responsive Bootstrap Theme for Appointment',
    'category': 'Theme/Appointment',
    'summary': '',
    'version': '1.0',
    'depends': ['base', 'website', 'portal', 'website_form'],
    'data': [
        'security/ir.model.access.csv',
        'data/additional_menu.xml',
        'data/appointment_fields.xml',
        'views/assets.xml',
        'views/appointment.xml',
        'views/patient.xml',
        'views/patient_details.xml',
        'views/appointment_slot.xml',
        'views/staff_details.xml',
        'views/footer.xml',
        'views/home.xml',
        'views/appointment_details.xml',
    ],
    'images': [
        'static/src/img/appointment_logo.jpg',
    ],
    'author': 'Bhavik Vaghela',
    'maintainer': 'Bhavik Vaghela',

    'application': False,
    'installable': True,
    'auto_install': False,

}
