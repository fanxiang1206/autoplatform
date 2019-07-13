from django.contrib import admin

from case.models import Case

# Register your models here.
class CaseAdmin(admin.ModelAdmin):
    list_display = ['name','url','method','header','param_type','params','assert_type','assert_params','creattime']
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Case,CaseAdmin)