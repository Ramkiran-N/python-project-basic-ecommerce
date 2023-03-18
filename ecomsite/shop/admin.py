from django.contrib import admin
from .models import Product,Order
# Register your models here.

admin.site.site_header = "Ecommerce Website"
admin.site.site_title = 'Ecommerce'
admin.site.index_title = "Manage Website"
class ProductAdmin(admin.ModelAdmin):
    def change_price_to_default(self,request,queryset):
        queryset.update(price='default')
    change_price_to_default.short_description = 'price default'
    list_display = ('title','price')
    search_fields = ('title','price')
    actions = ('change_price_to_default',)
    fields = ('title','price',)
    list_editable = ('price',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)