/** @odoo-module **/
/* ============================================= */
/*  تغيير عنوان Tab المتصفح                      */
/*  من "Odoo" إلى اسم النظام المخصص              */
/* ============================================= */

import { registry } from "@web/core/registry";
import { patch } from "@web/core/utils/patch";

// تغيير العنوان الافتراضي
const serviceRegistry = registry.category("services");

const titleService = {
    start() {
        let current = {};
        // تغيير "Odoo" إلى اسم النظام
        const setParts = (parts) => {
            current = Object.assign(current, parts);
            const title = Object.values(current).filter(Boolean).join(" - ");
            document.title = title || "نظام المستلزمات الطبية";
        };
        // حذف "Odoo" من العنوان
        const listener = () => {
            if (document.title.includes("Odoo")) {
                document.title = document.title.replace(/Odoo/gi, "نظام المستلزمات الطبية");
            }
        };
        // مراقبة تغييرات العنوان
        const observer = new MutationObserver(() => listener());
        observer.observe(document.querySelector('title'), { childList: true });
        // التشغيل الأولي
        listener();

        return {
            setParts,
            getParts() { return current; },
        };
    },
};

// محاولة تسجيل الخدمة (قد تكون مسجلة مسبقاً)
try {
    // استبدال كلمة Odoo في أي عنصر
    document.addEventListener("DOMContentLoaded", () => {
        setInterval(() => {
            if (document.title.includes("Odoo")) {
                document.title = document.title.replace(/Odoo/gi, "نظام المستلزمات الطبية");
            }
        }, 1000);
    });
} catch (e) {
    console.log("Medical theme: title service initialized");
}
