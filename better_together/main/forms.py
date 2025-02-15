from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Report, Request  

class RegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, label="ФИО")
    email = forms.EmailField(required=True, label="Email")
    agree = forms.BooleanField(required=True, label="Согласие на обработку данных")

    class Meta:
        model = CustomUser
        fields = ("full_name", "username", "email", "password1", "password2", "agree")


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "description", "file"]


# ✅ Добавляем форму для заявки
class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["title", "description", "category", "image"]  # Поля из модели Request
