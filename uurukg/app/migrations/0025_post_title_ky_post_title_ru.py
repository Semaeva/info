# Generated by Django 4.2.1 on 2023-06-15 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_post_title_ky_remove_post_title_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_ky',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=225, null=True),
        ),
    ]
