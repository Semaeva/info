# Generated by Django 4.2.1 on 2023-06-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_remove_post_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govnoimage',
            name='image',
            field=models.FileField(upload_to='govno/detail/'),
        ),
    ]