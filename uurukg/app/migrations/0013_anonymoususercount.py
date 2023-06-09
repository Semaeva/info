# Generated by Django 4.2.1 on 2023-06-13 08:33

from django.db import migrations, models
import hitcount.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_country_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnonymousUserCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(unique=True)),
            ],
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
    ]
