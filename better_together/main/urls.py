from django.contrib import admin
from django.urls import path
from main import views
from .views import register, create_request  
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('report/', views.report, name='report'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", register, name="register"),
    path('profile/', views.profile, name='profile'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("request/new/", create_request, name="submit_request"),
]
