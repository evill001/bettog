# Generated by Django 5.1.4 on 2025-02-15 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_request_photo_after_request_photo_before'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='image',
        ),
    ]
