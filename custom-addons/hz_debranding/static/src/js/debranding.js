/** @odoo-module **/
/* ============================================= */
/*  إزالة شاملة لهوية Odoo — الحسن زكريا         */
/* ============================================= */

const SYSTEM_NAME = "الحسن زكريا - المستلزمات الطبية";

// تغيير عنوان المتصفح
function replaceOdooInTitle() {
    if (document.title && document.title.indexOf("Odoo") !== -1) {
        document.title = document.title.replace(/Odoo/gi, SYSTEM_NAME);
    }
}

// مراقب عنوان الصفحة
try {
    const titleEl = document.querySelector("title");
    if (titleEl) {
        new MutationObserver(replaceOdooInTitle).observe(titleEl, {
            childList: true,
        });
    }
} catch (e) {
    // ignore
}

replaceOdooInTitle();
setInterval(replaceOdooInTitle, 3000);

// إخفاء روابط Odoo
setInterval(function () {
    var links = document.querySelectorAll('a[href*="odoo.com"]');
    for (var i = 0; i < links.length; i++) {
        links[i].style.display = "none";
    }
}, 5000);

// إخفاء "حسابي على أودو" وزر الشات ديناميكياً
function hideDebrandingElements() {
    // إخفاء "حسابي على أودو" من القائمة المنسدلة
    document.querySelectorAll('[data-menu="account"]').forEach(function (el) {
        el.style.display = "none";
    });
    // إخفاء عنصر قائمة يحتوي على نص "حسابي" أو "Odoo.com"
    document.querySelectorAll('.dropdown-item').forEach(function (el) {
        var text = el.textContent || "";
        if (text.indexOf("حسابي على") !== -1 || text.indexOf("My Odoo") !== -1 || text.indexOf("odoo.com") !== -1) {
            el.style.display = "none";
        }
    });
    // إخفاء زر الشات/الدردشة من systray
    document.querySelectorAll('.o-mail-DiscussSystray-class, .o-mail-DiscussSystray, .o-mail-MessagingMenu').forEach(function (el) {
        el.style.display = "none";
    });
}

setInterval(hideDebrandingElements, 2000);

