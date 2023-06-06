from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from embed_video.fields import EmbedVideoField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=250)

    # body = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', editable=False, max_length=160)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_p',
                                        related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)




class News(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField(default='')
    created_date = models.DateField(auto_now_add=True)
    order_date = models.DateField()
    image = models.ImageField(upload_to='newsImage/', blank=True, null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        verbose_name = "Новости"
        verbose_name_plural = "Новости"


class NewsImage(models.Model):
    image = models.ImageField(upload_to='news/detail/')
    news = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True, related_name='newsImage')

    def __str__(self):
        return f'название:{self.news.title}'

    class Meta:
        verbose_name = "Галерея Новости"
        verbose_name_plural = "Галерея Новостей"


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Govno(models.Model):
    name = models.CharField('Доп инфо', max_length=253, default='', blank=False, null=False)
    birth = models.DateField(default=datetime.today)
    position = models.CharField(max_length=253, default='неизвестно')
    department = models.CharField(max_length=250, default='неизвестно')
    resume = models.TextField(default='')
    dop_info = models.TextField(default='', blank=True, null=True)
    created_date = models.DateField('Дата события', auto_now_add=False)
    criminal_record = models.BooleanField(default=False)
    years = models.CharField(max_length=100)
    image = models.ImageField(upload_to='avatars/', blank=True, null=True)
    video = EmbedVideoField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"


class GovnoImage(models.Model):
    image = models.ImageField(upload_to='govno/detail/')
    govno = models.ForeignKey(News, on_delete=models.CASCADE, blank=True, null=True, related_name='govnoImage')

    def __str__(self):
        return f'название:{self.govno.title}'

    class Meta:
        verbose_name = "Галерея Дополнительной информации"
        verbose_name_plural = "Галерея Дополнительной информации"


class PageView(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content_object} - {self.timestamp}'
#113
