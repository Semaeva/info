# Generated by Django 4.2.1 on 2023-06-09 18:45

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_category_press_release_departments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Новости СНГ',
                'verbose_name_plural': 'Новости СНГ',
            },
        ),
        migrations.CreateModel(
            name='NewsSNG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('overview', ckeditor.fields.RichTextField()),
                ('created_date', models.DateField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='pressRelease/')),
                ('description', models.TextField(default='')),
                ('top_news', models.BooleanField(default=False)),
                ('sng', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
            options={
                'verbose_name': 'Новости СНГ',
                'verbose_name_plural': 'Новости СНГ',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsSngImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sng-news/detail/')),
                ('news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newsImage', to='app.newssng')),
            ],
            options={
                'verbose_name': 'Галерея Новостей СНГ',
                'verbose_name_plural': 'Галерея Новостей СНГ',
            },
        ),
        migrations.CreateModel(
            name='PressReleaseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='press-news/detail/')),
                ('press_release_news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='newsImage', to='app.press_release')),
            ],
            options={
                'verbose_name': 'Галерея Пресс-Релиз',
                'verbose_name_plural': 'Галерея Пресс-Релиз',
            },
        ),
        migrations.DeleteModel(
            name='PageView',
        ),
    ]
