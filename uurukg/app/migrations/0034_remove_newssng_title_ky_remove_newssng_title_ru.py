# Generated by Django 4.2.1 on 2023-06-19 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_remove_govno_criminal_record_ky_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newssng',
            name='title_ky',
        ),
        migrations.RemoveField(
            model_name='newssng',
            name='title_ru',
        ),
    ]
