from django.contrib import admin
from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'created_at',
        'updated_at',
    )

    fieldsets = (
        ('Produto', {
            'fields': (
                'name',
                'description',
                'price',
                'category',
            )
        }),
        ('Imagens', {
            'fields': (
                'image_1',
                'image_2',
                'image_3',
                'image_4',
                'image_5',
                'image_6',
            )
        }),
    )

    search_fields = ('name',)

    list_filter = (
        'category',
        'created_at',
        'updated_at',
    )

    ordering = (
        'name',
        'category',
        'price',
        'created_at',
        'updated_at',
    )

    class Meta:
        order_by = ('name',)
