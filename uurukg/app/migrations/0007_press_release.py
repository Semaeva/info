# Generated by Django 4.2.1 on 2023-06-09 13:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_post_slug_post_description_post_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Press_release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('overview', ckeditor.fields.RichTextField()),
                ('created_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='pressRelease/')),
                ('description', models.TextField(default='')),
                ('top_news', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
            options={
                'verbose_name': 'Пресс-Релизы',
                'verbose_name_plural': 'Пресс-Релизы',
                'ordering': ['-created_date'],
            },
        ),
    ]
