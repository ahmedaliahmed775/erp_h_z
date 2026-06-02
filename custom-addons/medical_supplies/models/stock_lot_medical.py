from odoo import models, fields, api
from datetime import date, timedelta


class StockLotMedical(models.Model):
    """إضافة حقول طبية لأرقام اللوت/الباتش"""
    _inherit = 'stock.lot'

    # ========================================
    #  معلومات اللوت الطبية
    # ========================================
    manufacturing_date = fields.Date(
        string='تاريخ التصنيع',
    )
    
    sterilization_date = fields.Date(
        string='تاريخ التعقيم',
        help='تاريخ آخر عملية تعقيم (للمنتجات المعقمة)',
    )
    
    batch_number = fields.Char(
        string='رقم الباتش',
        help='رقم دفعة الإنتاج من المصنع',
    )
    
    certificate_of_analysis = fields.Binary(
        string='شهادة التحليل (COA)',
        help='شهادة تحليل الجودة من الشركة المصنعة',
    )
    
    certificate_filename = fields.Char(
        string='اسم ملف الشهادة',
    )
    
    inspection_status = fields.Selection([
        ('pending', 'بانتظار الفحص'),
        ('passed', 'ناجح'),
        ('failed', 'فاشل'),
        ('quarantine', 'حجر'),
    ], string='حالة الفحص', default='pending')
    
    inspector_notes = fields.Text(
        string='ملاحظات المفتّش',
    )
    
    temperature_log = fields.Text(
        string='سجل درجة الحرارة',
        help='سجل درجة الحرارة أثناء الشحن والتخزين',
    )

    # ========================================
    #  حساب تلقائي لحالة الصلاحية
    # ========================================
    days_to_expiry = fields.Integer(
        string='الأيام المتبقية للصلاحية',
        compute='_compute_days_to_expiry',
        store=False,
    )
    
    expiry_status = fields.Selection([
        ('valid', 'صالح'),
        ('warning', 'قارب على الانتهاء'),
        ('expired', 'منتهي الصلاحية'),
    ], string='حالة الصلاحية', compute='_compute_days_to_expiry', store=False)

    @api.depends('expiration_date')
    def _compute_days_to_expiry(self):
        today = date.today()
        for lot in self:
            if lot.expiration_date:
                exp_date = lot.expiration_date
                if isinstance(exp_date, fields.Datetime):
                    exp_date = exp_date.date()
                delta = (exp_date - today).days
                lot.days_to_expiry = delta
                if delta <= 0:
                    lot.expiry_status = 'expired'
                elif delta <= 90:
                    lot.expiry_status = 'warning'
                else:
                    lot.expiry_status = 'valid'
            else:
                lot.days_to_expiry = 0
                lot.expiry_status = 'valid'
