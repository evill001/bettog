from django.contrib import admin
from .models import Request, Profile, Report

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "status", "created_at")  
    list_filter = ("status", "created_at")  
    search_fields = ("title", "description")  
    readonly_fields = ("created_at",)  

    def save_model(self, request, obj, form, change):
        # Блокируем изменение статуса, если он уже "Решена" или "Отклонена"
        if obj.pk:  # Если объект уже существует
            original = Request.objects.get(pk=obj.pk)
            if original.status in ["Решена", "Отклонена"]:
                return  # Не даём сохранить изменения
                
        super().save_model(request, obj, form, change) 

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")  
    search_fields = ("title", "description")  

admin.site.register(Profile)