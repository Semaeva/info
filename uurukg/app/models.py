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


class Post(models.Model, HitCountMixin):
    title = models.CharField(max_length=225)
    overview = RichTextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to='newsImage/', blank=True, null=True)
    description = models.TextField(default='')
    top_news = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'detail.html'
    # slug_field = "slug"
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hit_count'] = self.object.hit_count.hits
        return context


class Press_release(models.Model):
    title = models.CharField(max_length=225)
    overview = RichTextField()
    departments = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to='pressRelease/', blank=True, null=True)
    description = models.TextField(default='')
    top_news = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Пресс-Релизы"
        verbose_name_plural = "Пресс-Релизы"


class NewsSNG(models.Model):
    title = models.CharField(max_length=225)
    overview = RichTextField()
    sng = models.ForeignKey("Country", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateField(auto_now_add=False)
    image = models.ImageField(upload_to='pressRelease/', blank=True, null=True)
    description = models.TextField(default='')
    top_news = models.BooleanField(default=False)

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
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Department(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Министерства и учреждения"
        verbose_name_plural = "Министерства и учреждения"


class Country(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости СНГ"
        verbose_name_plural = "Новости СНГ"


class Govno(models.Model):
    name = models.CharField('ФИО', max_length=253, default='', blank=False, null=False)
    birth = models.DateField(default=datetime.today)
    position = models.CharField(max_length=253, default='неизвестно')
    department = models.CharField(max_length=250, default='неизвестно')
    resume = models.TextField(default='')
    dop_info = models.TextField(default='', blank=True, null=True)
    created_date = models.DateField('Дата события', auto_now_add=False)
    criminal_record = models.BooleanField(default=False)
    years = models.CharField(max_length=100)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"


class GovnoImage(models.Model):
    image = models.ImageField(upload_to='govno/detail/')
    govno = models.ForeignKey(Govno, on_delete=models.CASCADE, blank=True, null=True, related_name='govnoImage')

    def __str__(self):
        return f'название:{self.govno.title}'

    class Meta:
        verbose_name = "Галерея Дополнительной информации"
        verbose_name_plural = "Галерея Дополнительной информации"


# class PageView(models.Model):
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.CharField(max_length=255)
#     content_object = GenericForeignKey('content_type', 'object_id')
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.content_object} - {self.timestamp}'
#113
