from django.contrib import admin 
# Register your models here.
from .models import Category,Brand ,Product, Firm, Stock
 
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Stock)