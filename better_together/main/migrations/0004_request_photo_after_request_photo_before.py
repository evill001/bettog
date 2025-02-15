# Generated by Django 5.1.4 on 2025-02-15 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_report_image_after_report_image_before_report_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='photo_after',
            field=models.ImageField(blank=True, null=True, upload_to='requests/after/', verbose_name='Фото после'),
        ),
        migrations.AddField(
            model_name='request',
            name='photo_before',
            field=models.ImageField(blank=True, null=True, upload_to='requests/before/', verbose_name='Фото до'),
        ),
    ]
