# Generated by Django 5.1.3 on 2024-11-21 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0021_propertyimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyimage',
            old_name='property',
            new_name='propertys',
        ),
    ]