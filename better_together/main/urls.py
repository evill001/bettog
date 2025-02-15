from django.contrib import admin
from django.urls import path
from main import views
from .views import register, create_request, profile, delete_request, update_request_status
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('reports/', views.reports, name='reports'),
    path('report/', views.report, name='report'),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("request/new/", create_request, name="submit_request"),
    path("request/<int:request_id>/delete/", delete_request, name="delete_request"),
    path("request/<int:request_id>/update_status/", update_request_status, name="update_request_status"),
]
