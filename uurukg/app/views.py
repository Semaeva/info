import hitcount.models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from hitcount.models import Hit

from .models import *
from django.db.models import Q
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.contrib.contenttypes.models import ContentType
from hitcount.views import HitCountDetailView

from django.views.generic.detail import DetailView
from autoslug import AutoSlugField


def list_top_news():
    top_list=list()
    for i in list(HitCount.objects.all()):
        top_list.append(i.hits)
    list_sort = sorted(top_list)
    top_three = list_sort[-3:]
    return top_three


def posts(request):
    data = list()
    posts = Post.objects.all()
    newsEcnom = Post.objects.filter(category=2).all()
    newsSport = Post.objects.filter(category=3).all()
    newsCriminal = Post.objects.filter(category=1).all()
    top = list(HitCount.objects.filter(hits__range=(list_top_news()[0], list_top_news()[-1])).all())[-2:]
    for i in HitCount.objects.all():
        data.append(i.object_pk)
    #print(i.object_pk)

    return render(request, "blog.html", {'posts': posts,
                                         'newsEconom': newsEcnom,
                                         'newsSport': newsSport,
                                         'newsCriminal': newsCriminal,
                                         'top': top
                                       })


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post.html'
    slug_field = "slug"
    count_hit = True

    def __str__(self):
        return  self.count_hit

# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = "post.html"
#     slug_field = "slug"

# class PostDetailView(HitCountDetailView):
#     model = News
#     template_name = 'econom.html'
#     slug_field = "slug"
#     count_hit = True


def news_list(request):
    news = News.objects.order_by('-id')[:5]
    newsImg = NewsImage.objects.all()
    newsTop = News.objects.all()
    newsEcnom = News.objects.filter(category= 1 ).all()
    newsSport = News.objects.filter(category= 3 ).all()
    newsCriminal = News.objects.filter(category= 2 ).all()
    return render(request, 'index.html', {'news': news,
                                          'newsImg':newsImg,
                                          'newsEcnom':newsEcnom,
                                          'newsCriminal': newsCriminal,
                                          'newsSport': newsSport
                                          })


# def word_list():
#     word_lists_name = tuple(Govno.objects.values_list('name', flat=True))
#     word_lists_position = tuple(Govno.objects.values_list('position', flat=True))
#     return word_lists_name+word_lists_position

def economic_list(request):
    news = News.objects.filter(category= 1 ).all()
    return render(request, 'econom.html', {'news':news})


class NewsDetailView(DetailView):
    model = News
    template_name = "detail_news.html"
    slug_field = "slug"


def search(request):
    person = process.extract(request.POST.get("name", "Undefined"),
                             list(Govno.objects.values_list('name', flat=True)),
                             scorer=fuzz.token_sort_ratio)
    position = process.extract(request.POST.get("position", "Undefined"),
                               list(Govno.objects.values_list('position', flat=True)),
                               scorer=fuzz.token_sort_ratio)
    data = list()

    for i in person:
        if int(i[1]) > 50:
            data.append(i[0])
    for ii in position:
        if ii[1] > 50:
            data.append(ii[0])
    print(f'my data ={data}')
    if data:
        for i in data:
            persons = Govno.objects.filter(Q(name=i) | Q(position=i))
            print(data)
            return render(request, 'search_result.html', {'person': persons})
    else:
        return render(request, 'search_result.html', {'person': 0})


def my_view(request):
    current_url = request.path
    content_type = ContentType.objects.get_for_model(PageView)

    # Увеличить счетчик просмотров
    PageView.objects.create(
        content_type=content_type,
        object_id=current_url,
    )
    # return render(request, 'my_template.html')
    return HttpResponse("Страница")


# def get_page_views(url):
#         content_type = ContentType.objects.get_for_model(PageView)
#     page_views_count = PageView.objects.filter(
#         content_type=content_type,
#         object_id=url,
#     ).count()
#     return page_views_count
#
#
# def count_view():
#     page_url = "/my-page/"
#     views_count = get_page_views(page_url)
#     print(f"Количество просмотров страницы {page_url}: {views_count}")