from django.contrib import admin
from project.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','creattime']
    list_filter = ['status']
    search_fields = ['name']

admin.site.register(Project,ProjectAdmin)