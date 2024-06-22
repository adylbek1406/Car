from django.contrib import admin
from .models import Car


#
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_filter = ['price','name']
    search_fields = ['name']


admin.site.register(Car, CarAdmin)
