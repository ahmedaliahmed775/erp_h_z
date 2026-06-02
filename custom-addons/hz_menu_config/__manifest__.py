{
    'name': 'الحسن زكريا - تخصيص القوائم',
    'version': '17.0.1.0.0',
    'category': 'Tools',
    'summary': 'تخصيص القوائم والتطبيقات المعروضة حسب حاجة شركة المستلزمات الطبية',
    'description': """
        تخصيص القوائم لشركة الحسن زكريا:
        - تعريب أسماء القوائم الرئيسية
        - إخفاء التطبيقات غير المطلوبة
        - ترتيب القوائم حسب أولوية العمل
        - تخصيص الوصول للمستخدمين
    """,
    'author': 'الحسن زكريا للمستلزمات الطبية',
    'website': '',
    'depends': [
        'base',
        'sale_management',
        'purchase',
        'stock',
        'account',
        'contacts',
        'hr',
        'mail',
        'base_accounting_kit',
        'medical_supplies',
        'hz_debranding',
    ],
    'data': [
        'views/menu_customization.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
