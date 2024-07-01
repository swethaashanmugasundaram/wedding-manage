from django.contrib import admin
from .models import *



# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','image','description')
    
admin.site.register(Wedding,VendorAdmin)
admin.site.register(Traditional)
admin.site.register(Carts)
admin.site.register(Favourite)
admin.site.register(Order)
admin.site.register(OdrderItem)



