# Generated by Django 5.1.3 on 2024-11-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0016_companyinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='map_link',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]