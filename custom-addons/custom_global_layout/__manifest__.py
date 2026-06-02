{
    'name': 'الحسن زكريا - القالب الموحّد للمستندات',
    'version': '17.0.3.0.0',
    'category': 'Customizations',
    'summary': 'قالب موحّد احترافي لجميع تقارير ومستندات النظام بهوية الحسن زكريا',
    'description': """
        القالب الموحّد الشامل:
        - هيدر وفوتر موحّد لجميع المستندات (21 تقرير)
        - تصميم احترافي بهوية الحسن زكريا
        - دعم كامل للغة العربية (RTL)
        - تعريب عناوين جداول جميع التقارير
        - قسم توقيعات موحّد في كل مستند
        - ألوان وخطوط موحّدة عبر CSS مركزي
        - حماية: منع المستخدمين من تعديل القوالب
    """,
    'author': 'الحسن زكريا للمستلزمات الطبية',
    'depends': [
        'base',
        'web',
        'account',
        'sale_management',
        'purchase',
        'stock',
        'om_hr_payroll',
        'hr_expense',
        'base_accounting_kit',
    ],
    'data': [
        # === التخطيط العام (الهيدر والفوتر) ===
        'views/layout_template.xml',

        # === الفواتير والمبيعات ===
        'report/report_invoice.xml',
        'report/report_sale_order.xml',
        'report/report_payment_receipt.xml',

        # === المشتريات ===
        'report/report_purchase_order.xml',

        # === المخزون ===
        'report/report_delivery_slip.xml',
        'report/report_picking.xml',
        'report/report_inventory.xml',

        # === الرواتب والموارد البشرية ===
        'report/report_payslip.xml',
        'report/report_payslip_details.xml',
        'report/report_contribution_register.xml',
        'report/report_expense.xml',

        # === تقارير المحاسبة (base_accounting_kit) ===
        'report/report_general_ledger.xml',
        'report/report_trial_balance.xml',
        'report/report_cash_flow.xml',
        'report/report_partner_ledger.xml',
        'report/report_aged_partner.xml',
        'report/report_journal_audit.xml',
        'report/report_tax.xml',
        'report/report_day_book.xml',
        'report/report_bank_book.xml',
        'report/report_cash_book.xml',
        'report/report_financial.xml',

        # === الحماية ===
        'security/report_protection.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'custom_global_layout/static/src/css/report_global.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
