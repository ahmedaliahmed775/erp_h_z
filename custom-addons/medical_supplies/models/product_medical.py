from odoo import models, fields, api
from datetime import timedelta


class ProductTemplateMedical(models.Model):
    """إضافة حقول طبية خاصة لقالب المنتج"""
    _inherit = 'product.template'

    # ========================================
    #  معلومات التسجيل والتصنيف الطبي
    # ========================================
    medical_registration_no = fields.Char(
        string='رقم التسجيل الطبي',
        help='رقم تسجيل المنتج لدى الجهة التنظيمية (مثل SFDA)',
    )
    
    manufacturer_name = fields.Char(
        string='الشركة المصنّعة',
    )
    
    country_of_origin = fields.Many2one(
        'res.country',
        string='بلد المنشأ',
    )
    
    medical_classification = fields.Selection([
        ('disposable', 'مستهلكات طبية'),
        ('equipment', 'أجهزة ومعدات'),
        ('reagent', 'كواشف مخبرية'),
        ('implant', 'مواد زراعية'),
        ('ppe', 'معدات وقاية شخصية'),
        ('surgical', 'مستلزمات جراحية'),
        ('diagnostic', 'أجهزة تشخيصية'),
        ('pharma', 'مستحضرات صيدلانية'),
    ], string='التصنيف الطبي')
    
    risk_class = fields.Selection([
        ('class_1', 'الفئة الأولى - خطورة منخفضة'),
        ('class_2', 'الفئة الثانية - خطورة متوسطة'),
        ('class_3', 'الفئة الثالثة - خطورة عالية'),
        ('class_4', 'الفئة الرابعة - خطورة عالية جداً'),
    ], string='فئة الخطورة')
    
    is_sfda_approved = fields.Boolean(
        string='معتمد من هيئة الغذاء والدواء',
        default=False,
    )
    
    sfda_approval_no = fields.Char(
        string='رقم اعتماد SFDA',
    )

    # ========================================
    #  ظروف التخزين والصلاحية
    # ========================================
    storage_condition = fields.Selection([
        ('room_temp', 'درجة حرارة الغرفة (15-25°C)'),
        ('cool', 'تخزين بارد (2-8°C)'),
        ('frozen', 'تجميد (-20°C)'),
        ('deep_frozen', 'تجميد عميق (-80°C)'),
        ('controlled', 'ظروف خاصة'),
    ], string='ظروف التخزين', default='room_temp')
    
    storage_notes = fields.Text(
        string='ملاحظات التخزين',
        help='تعليمات خاصة للتخزين والتداول',
    )
    
    shelf_life_months = fields.Integer(
        string='مدة الصلاحية (بالأشهر)',
        help='مدة صلاحية المنتج من تاريخ التصنيع',
    )
    
    min_remaining_shelf_life = fields.Integer(
        string='الحد الأدنى المتبقي للصلاحية (بالأيام)',
        help='الحد الأدنى للأيام المتبقية قبل انتهاء الصلاحية لقبول المنتج',
        default=90,
    )

    # ========================================
    #  معلومات الاستيراد
    # ========================================
    hs_code = fields.Char(
        string='رمز النظام المنسّق (HS Code)',
        help='رمز التصنيف الجمركي',
    )
    
    customs_tariff = fields.Float(
        string='الرسوم الجمركية (%)',
    )
    
    import_license_required = fields.Boolean(
        string='يتطلب رخصة استيراد',
        default=False,
    )

    # ========================================
    #  تنبيهات المخزون
    # ========================================
    min_stock_qty = fields.Float(
        string='الحد الأدنى للمخزون',
        help='التنبيه عندما يصل المخزون لهذا المستوى',
    )
    
    max_stock_qty = fields.Float(
        string='الحد الأقصى للمخزون',
    )
    
    reorder_point = fields.Float(
        string='نقطة إعادة الطلب',
        help='يتم إنشاء أمر شراء تلقائي عند الوصول لهذا المستوى',
    )
