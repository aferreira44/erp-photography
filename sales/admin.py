from django.contrib import admin
from .models import Service, Product, Invoice, InvoiceProduct, InvoiceService


class InvoiceProductInline(admin.TabularInline):
    model = InvoiceProduct
    extra = 1


class InvoiceServiceInline(admin.TabularInline):
    model = InvoiceService
    extra = 1


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [
        InvoiceProductInline,
        InvoiceServiceInline,
    ]


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Service)
admin.site.register(Product)