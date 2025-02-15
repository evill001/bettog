from django.contrib import admin
from .models import Request, Profile, Report

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "created_at")  
    list_filter = ("status", "created_at")  
    search_fields = ("title", "description")  
    readonly_fields = ("created_at",)  

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")  
    search_fields = ("title", "description")  

admin.site.register(Profile)