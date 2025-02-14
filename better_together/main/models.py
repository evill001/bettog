from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с пользователем Django
    phone = models.CharField(max_length=15, blank=True, null=True)  # Телефон (необязательный)
    address = models.TextField(blank=True, null=True)  # Адрес (необязательный)

    def __str__(self):
        return self.user.username

class Request(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто подал заявку
    title = models.CharField(max_length=255)  # Название заявки
    description = models.TextField()  # Описание
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')  # Статус
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(self):
        return f"{self.title} - {self.get_status_display()}"
