from django.contrib import admin
from .models.product import Product
from .models.subproduct import SubProduct
from .models.customer import Customer


# displaying on the admin panel

class AdminProduct(admin.ModelAdmin):
    list_display = ['title']


class AdminSubProduct(admin.ModelAdmin):
    list_display = ['title', 'product']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['Hospital_Name', 'Hospital_Id', 'UserType']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(SubProduct, AdminSubProduct)
admin.site.register(Customer, AdminCustomer)
