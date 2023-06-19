from datetime import datetime
from msilib.schema import ListView

from django.utils import timezone as tz

from autoslug import AutoSlugField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.views.generic import DetailView
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount
from hitcount.views import HitCountDetailView
from modeltranslation.fields import TranslationField


class Post(models.Model, HitCountMixin):
    title = models.CharField('Наименование', max_length=225)
    overview = RichTextField('Полное описание')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Категории новостей')
    created_date = models.DateField('Дата создания', auto_now_add=False)
    image = models.ImageField('Главное изображение', upload_to='newsImage/', blank=False, null=False)
    description = models.TextField('Краткое описание', default='', max_length=180, blank=False, null=False)
    top_news = models.BooleanField('Входит в топ-новостей', default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class Press_release(models.Model):
    title = models.CharField('Наименование', max_length=225)
    overview = RichTextField('Полное описание')
    departments = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Министерство/учреждениеы')
    created_date = models.DateField(auto_now_add=False, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='pressRelease/',  blank=False, null=False, verbose_name='Главное изображение')
    description = models.TextField(default='', verbose_name='Краткое описание')
    top_news = models.BooleanField(default=False, verbose_name='Входит в топ-новостей')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Пресс-Релизы"
        verbose_name_plural = "Пресс-Релизы"


class NewsSNG(models.Model):
    title = models.CharField('Наименование', max_length=225)
    overview = RichTextField('Полное описание')
    sng = models.ForeignKey("Country", on_delete=models.CASCADE, blank=True, null=True, verbose_name='Страна')
    created_date = models.DateField(auto_now_add=False, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='pressRelease/',  blank=False, null=False, verbose_name='Главное изображение')
    description = models.TextField(default='', verbose_name='Краткое описание')
    top_news = models.BooleanField(default=False, verbose_name='Входит в топ-новостей')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Новости СНГ"
        verbose_name_plural = "Новости СНГ"


class NewsImage(models.Model):
    image = models.ImageField(upload_to='news/detail/')
    news = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True, related_name='newsImage')

    def __str__(self):
        return f'название:{self.news.title}'

    class Meta:
        verbose_name = "Галерея Новости"
        verbose_name_plural = "Галерея Новостей"


class PressReleaseImage(models.Model):
    image = models.ImageField(upload_to='press-news/detail/')
    press_release_news = models.ForeignKey(Press_release, on_delete=models.CASCADE, blank=True, null=True, related_name='pressReleaseImage')

    def __str__(self):
        return f'название:{self.press_release_news.title}'

    class Meta:
        verbose_name = "Галерея Пресс-Релиз"
        verbose_name_plural = "Галерея Пресс-Релиз"


class NewsSngImage(models.Model):
    image = models.ImageField(upload_to='sng-news/detail/')
    news = models.ForeignKey(NewsSNG, on_delete=models.CASCADE, blank=True, null=True, related_name='newsSNGImage')

    def __str__(self):
        return f'название:{self.news.title}'

    class Meta:
        verbose_name = "Галерея Новостей СНГ"
        verbose_name_plural = "Галерея Новостей СНГ"


class Category(models.Model):
    title = models.CharField('Наименование категории', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Department(models.Model):
    title = models.CharField('Наименование', max_length=200)
    image = models.ImageField(upload_to='departments/logo/',  blank=False, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Министерства и учреждения"
        verbose_name_plural = "Министерства и учреждения"


class Country(models.Model):
    title = models.CharField('Наименование', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страны СНГ"
        verbose_name_plural = "Страны СНГ"


class Govno(models.Model, HitCountMixin):
    name = models.CharField('ФИО', max_length=253, default='', blank=False, null=False)
    birth = models.DateField("Дата рождения", default=datetime.today)
    position = models.CharField('Должность', max_length=253, default='неизвестно')
    department = models.CharField('Место работы', max_length=250, default='неизвестно')
    # resume = models.TextField(default='')
    # dop_info = models.TextField(default='', blank=True, null=True)
    resume = RichTextField('Основная деятесльность')
    dop_info = RichTextField('Дополнительная информация')
    created_date = models.DateField('Дата события', auto_now_add=False)
    criminal_record = models.BooleanField('Судимость', default=False)
    years = models.CharField('Годы судимости', max_length=100)
    image = models.ImageField('Фотографии', upload_to='avatars/',  blank=False, null=False)
    video = EmbedVideoField('Ссылка на видео', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"


class GovnoImage(models.Model):
    image = models.ImageField(upload_to='govno/detail/')
    govno = models.ForeignKey(Govno, on_delete=models.CASCADE, blank=True, null=True, related_name='govnoImage')

    def __str__(self):
        return f'название:{self.govno.name}'

    class Meta:
        verbose_name = "Галерея Дополнительной информации"
        verbose_name_plural = "Галерея Дополнительной информации"


class AnonymousUserCount(models.Model, HitCountMixin):
    ip_address = models.GenericIPAddressField(unique=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    created_date = models.DateTimeField(auto_now=True)

