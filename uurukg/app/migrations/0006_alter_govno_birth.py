# Generated by Django 4.2.1 on 2023-06-05 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_govnoimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='govno',
            name='birth',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]