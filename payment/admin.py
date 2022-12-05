from django.contrib import admin
from .models import Item, Order, Discount


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    list_filter = ("name", "price")
    search_fields = ("name",)


admin.site.register(Item, ItemAdmin)
admin.site.register(Order)
admin.site.register(Discount)
