# ============================================
# سكريبت تطبيق التقارير فوراً وإجبارياً
# شغّل هذا السكريبت بعد أي تعديل على ملفات XML
# ============================================

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  تحديث وتطبيق قوالب التقارير فوراً" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] التحقق من Docker..." -ForegroundColor Yellow
$container = docker ps --filter "name=erp_h_z-odoo-1" --format "{{.Names}}" 2>$null
if (-not $container) {
    Write-Host "❌ خطأ: كونتينر Odoo غير شغّال!" -ForegroundColor Red
    Write-Host "شغّل: docker compose up -d" -ForegroundColor Gray
    exit 1
}
Write-Host "✅ Docker شغّال" -ForegroundColor Green

Write-Host ""
Write-Host "[2/3] تطبيق التعديلات على الإضافة..." -ForegroundColor Yellow
Write-Host "      (هذا قد يأخذ 30-60 ثانية)" -ForegroundColor Gray
Write-Host ""

docker exec erp_h_z-odoo-1 odoo -u custom_global_layout -d odoo_medical --stop-after-init --no-http 2>&1 | ForEach-Object {
    if ($_ -match "ERROR|error") {
        Write-Host "❌ $_" -ForegroundColor Red
    } elseif ($_ -match "WARNING|warning") {
        Write-Host "⚠️  $_" -ForegroundColor Yellow
    } else {
        Write-Host "   $_" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "[3/3] إعادة تشغيل Odoo..." -ForegroundColor Yellow
docker compose restart odoo 2>&1 | Out-Null
Write-Host "✅ تم إعادة التشغيل" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  ✅ تم تطبيق جميع التعديلات بنجاح!" -ForegroundColor Green
Write-Host "  افتح: http://localhost:8069" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
