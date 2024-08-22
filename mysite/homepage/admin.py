from django.contrib import admin
from .models import Purchase

# Register your models here.
# Model shows up in admin page

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("store", "purchase_date", "amount_spent", "products")
    search_fields = ("store", "products")
    
admin.site.register(Purchase, PurchaseAdmin)