from django.contrib import admin
from cafeteria.models import Station, Food, Order


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'station')

class OrderAdmin(admin.ModelAdmin):
    #list_display = ('user', '')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Station)
admin.site.register(Food, FoodAdmin)
admin.site.register(Order, OrderAdmin)
