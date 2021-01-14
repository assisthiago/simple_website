from django.contrib import admin, messages

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['set_most_wanted']

    list_display = (
        'name',
        'category',
        'price',
        'wanted',
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
                'wanted',
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

    readonly_fields = ('wanted',)

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
        'wanted',
        'created_at',
        'updated_at',
    )

    def set_most_wanted(self, request, queryset):
        if len(queryset) > 4:
            return messages.warning(request, 'Devem ser selecionados no máximo 4 itens a fim de executar a ação sobre eles.')

        Product.objects.filter(wanted=True).update(wanted=False)
        queryset.update(wanted=True)

        return messages.success(request, 'Os itens foram atualizados.')

    set_most_wanted.short_description = 'Colocar como "Mais procurados"'

    class Meta:
        order_by = ('name',)
