from django.contrib import admin
from .models import User, Seller, Product

# Register your models here.
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Product)