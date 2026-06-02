{
    'name': 'إدارة المستلزمات الطبية',
    'version': '17.0.1.0.0',
    'category': 'Inventory/Medical',
    'summary': 'نظام متكامل لإدارة المستلزمات الطبية — تتبع الصلاحيات واللوت والتخزين',
    'description': """
        موديول مخصص لشركات استيراد وتوزيع المستلزمات الطبية:
        
        الميزات:
        - حقول طبية إضافية للمنتجات (رقم التسجيل، الشركة المصنعة، بلد المنشأ)
        - تصنيف طبي للمنتجات (مستهلكات، أجهزة، كواشف)
        - ظروف التخزين (عادي، مبرّد، مجمّد)
        - تنبيهات انتهاء الصلاحية
        - فئات منتجات طبية جاهزة
        - وحدات قياس طبية
        - تقارير مخصصة
    """,
    'author': 'Medical ERP Solutions',
    'website': '',
    'depends': [
        'product',
        'stock',
        'product_expiry',
        'purchase',
        'sale_management',
        'contacts',
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/product_categories.xml',
        'data/uom_data.xml',
        'views/product_views.xml',
        'views/stock_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
