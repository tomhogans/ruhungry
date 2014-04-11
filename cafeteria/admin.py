from django.contrib import admin
from ruhungry.models import Station, Food, Order


class OrderAdmin(admin.ModelAdmin):
    #list_display = ('user', '')
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Station)
admin.site.register(Food)
admin.site.register(Order, OrderAdmin)
