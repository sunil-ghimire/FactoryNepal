from django.contrib import admin
from .models import User, Seller, Product, ProductCategory, ProductSubCategory

from django.contrib import admin

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'full_name']


class SellerAdmin(admin.ModelAdmin):
    list_display = ['company_name',
                    'company_phone', 'company_email']
    search_fields=['company_name', 'company_email', 'company_phone', 'company_address', 'company_city', 'company_state', 'company_country', 'company_zip']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'image', 'seller']
    list_filter = ['seller','category','sub_category','is_admin_approved']
    search_fields = ['name', 'description']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(User, UserAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductSubCategory, ProductSubCategoryAdmin)
