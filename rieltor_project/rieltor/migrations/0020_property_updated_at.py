# Generated by Django 5.1.3 on 2024-11-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rieltor', '0019_alter_faq_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]