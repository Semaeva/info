# Generated by Django 4.2.1 on 2023-06-13 12:30

import ckeditor.fields
import datetime
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_govno_dop_info_alter_govno_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsimage',
            name='image',
        ),
        migrations.AddField(
            model_name='newsimage',
            name='images',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='country',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='birth',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='criminal_record',
            field=models.BooleanField(default=False, verbose_name='Судимость'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='department',
            field=models.CharField(default='неизвестно', max_length=250, verbose_name='Место работы'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='dop_info',
            field=ckeditor.fields.RichTextField(verbose_name='Дополнительная информация'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='position',
            field=models.CharField(default='неизвестно', max_length=253, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='resume',
            field=ckeditor.fields.RichTextField(verbose_name='Основная деятесльность'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True, verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='govno',
            name='years',
            field=models.CharField(max_length=100, verbose_name='Годы судимости'),
        ),
    ]
