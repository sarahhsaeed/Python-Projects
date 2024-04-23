from django.contrib import admin
from .models import products,Offer
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','discount')

admin.site.register(products,ProductAdmin) 
admin.site.register(Offer,OfferAdmin) 