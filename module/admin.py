from django.contrib import admin
from module.models import Module

# Register your models here.


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describe','creattime']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Module,ModuleAdmin)