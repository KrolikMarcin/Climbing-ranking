from django.contrib import admin
from ascents.models import Route, Ascent

# Register your models here.



class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    ordering = ['last_name']

class RouteAdmin(admin.ModelAdmin):
    search_fields = ['name']
    ordering = ['name']

class AscentAdmin(admin.ModelAdmin):
    search_fields = ['user.name']


admin.site.register(Route, RouteAdmin)
admin.site.register(Ascent, AscentAdmin)