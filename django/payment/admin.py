from django.contrib import admin
from .models import *

admin.site.register(PaymentAllocation)

class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "status",
        "created_at",
        "days_since_creation",
        "shamsi_date",
    )
    search_fields = ("authority", "ref_id", "amount")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)

    def days_since_creation(self, obj):
        return obj.days_since_creation()

    days_since_creation.short_description = "روزهای گذشته از ایجاد"

    def shamsi_date(self, obj):
        return obj.shamsi_date

    shamsi_date.short_description = "تاریخ شمسی"


admin.site.register(Payment, PaymentAdmin)


class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "balance",
        "created_at",
        "updated_at",
        "shamsi_created",
        "shamsi_updated",
        "action_count",
    )
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")

    def shamsi_created(self, obj):
        return obj.shamsi_created

    shamsi_created.short_description = "تاریخ ایجاد شمسی"

    def shamsi_updated(self, obj):
        return obj.shamsi_updated

    shamsi_updated.short_description = "تاریخ بروزرسانی شمسی"


admin.site.register(Wallet, WalletAdmin)
