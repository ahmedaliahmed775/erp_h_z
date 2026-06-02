{
    'name': 'الحسن زكريا - إزالة هوية أودو',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'إزالة شاملة لجميع إشارات Odoo واستبدالها بهوية الحسن زكريا',
    'description': """
        موديول إزالة هوية Odoo بالكامل:
        - إزالة كل النصوص والشعارات التي تشير إلى Odoo
        - تغيير عنوان Tab المتصفح
        - تخصيص رسائل النظام
        - إخفاء روابط Odoo.com
        - تغيير اسم النظام في كل مكان
    """,
    'author': 'الحسن زكريا للمستلزمات الطبية',
    'website': '',
    'depends': ['web', 'base', 'mail', 'base_setup', 'point_of_sale'],
    'data': [
        'views/webclient_templates.xml',
        'views/login_page.xml',
        'views/ir_module_views.xml',
        'data/res_company_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hz_debranding/static/src/css/debranding.css',
            'hz_debranding/static/src/css/premium_theme.css',
            'hz_debranding/static/src/js/debranding.js',
            'hz_debranding/static/src/xml/systray.xml',
        ],
        'web.assets_frontend': [
            'hz_debranding/static/src/css/login.css',
        ],
        'point_of_sale._assets_pos': [
            'hz_debranding/static/src/css/pos_theme.css',
            'hz_debranding/static/src/xml/pos_navbar.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
