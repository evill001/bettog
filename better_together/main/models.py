from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Request(models.Model):
    CATEGORY_CHOICES = [
        ('Техническая', 'Техническая'),
        ('Финансовая', 'Финансовая'),
        ('Общая', 'Общая'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(  # Исправил опечатку "ategory" -> "category"
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория",
        default="Техническая"
    )
    image = models.ImageField(upload_to='requests/', blank=True, null=True, verbose_name="Фотография")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=[('Ожидание', 'Ожидание'), ('Решено', 'Решено')], default='Ожидание', verbose_name="Статус")

    def __str__(self):
        return self.title

class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Заменил `User` на `settings.AUTH_USER_MODEL`
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to="reports/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
