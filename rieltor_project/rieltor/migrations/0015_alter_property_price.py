# Generated by Django 5.1.3 on 2024-11-13 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0014_client_property_alter_property_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
