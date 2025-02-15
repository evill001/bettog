from django.contrib import admin
from .models import Request, Profile, Report

admin.site.register(Request)
admin.site.register(Profile)
admin.site.register(Report)