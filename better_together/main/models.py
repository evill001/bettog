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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    CATEGORY_CHOICES = [
        ('Техническая', 'Техническая'),
        ('Финансовая', 'Финансовая'),
        ('Общая', 'Общая'),
    ]

    STATUS_CHOICES = [
    ('Новая', 'Новая'),
    ('Решена', 'Решена'),
    ('Отклонена', 'Отклонена'),
    ]

    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Категория",
        default="Техническая"
    )
    photo_before = models.ImageField(upload_to='requests/before/', blank=True, null=True, verbose_name="Фото до")
    photo_after = models.ImageField(upload_to='requests/after/', blank=True, null=True, verbose_name="Фото после")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Новая', verbose_name="Статус")

    def __str__(self):
        return self.title


class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Автор заявки
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    file = models.FileField(upload_to="reports/", blank=True, null=True, verbose_name="Файл")
    image_before = models.ImageField(upload_to="reports/before/", blank=True, null=True, verbose_name="Фото до")
    image_after = models.ImageField(upload_to="reports/after/", blank=True, null=True, verbose_name="Фото после (заполняет админ)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    STATUS_CHOICES = [
        ("pending", "В ожидании"),
        ("resolved", "Решено"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", verbose_name="Статус")

    def __str__(self):
        return self.title
