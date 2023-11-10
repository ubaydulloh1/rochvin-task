from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'quantity',
        'price',
    )
    list_display_links = (
        'pk',
        'name',
    )
    search_fields = (
        'name',
    )


class OrderProductInline(admin.TabularInline):
    model = models.OrderProduct
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'client',
        'employee',
        'total_price',
        'ordered_at',
    )
    list_display_links = (
        'pk',
        'client',
    )
    search_fields = (
        'client__first_name',
        'client__last_name',
        'employee__first_name',
        'employee__last_name',
    )
    autocomplete_fields = (
        'client',
        'employee',
        'products',
    )
    inlines = (
        OrderProductInline,
    )
