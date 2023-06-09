import hitcount.models
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from hitcount.models import Hit

from .models import *
from django.db.models import Q
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.contrib.contenttypes.models import ContentType
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount
from django.views.generic.detail import DetailView


def list_top_news():
    data = list()
    # top_list=list()
    # for i in list(HitCount.objects.all()):
    #     top_list.append(i.hits)
    for i in HitCount.objects.all():
        data.append(i.object_pk)
    if data:
        sort_data = sorted(data)
        tt = Post.objects.filter(id__range=(data[0], sort_data.pop()))
        return tt
    else:
        return 0


def posts(request):
    posts = Post.objects.all()
    newsEcnom = Post.objects.filter(category=2).all()
    newsSport = Post.objects.filter(category=3).all()
    newsCriminal = Post.objects.filter(category=1).all()
    newsTop = Post.objects.filter(top_news=True).all()[:4]
    return render(request, "index.html", {'posts': posts,
                                         'newsEconom': newsEcnom,
                                         'newsSport': newsSport,
                                         'newsCriminal': newsCriminal,
                                         'top': newsTop
                                       })


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'detail.html'
    count_hit = True


#
# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = 'post.html'
#     slug_field = "slug"
#     count_hit = True

    # def __str__(self):
    #     return self.count_hit


# def news_list(request):
#     news = News.objects.order_by('-id')[:5]
#     newsImg = NewsImage.objects.all()
#     newsTop = News.objects.all()
#     newsEcnom = News.objects.filter(category= 1 ).all()
#     newsSport = News.objects.filter(category= 3 ).all()
#     newsCriminal = News.objects.filter(category= 2 ).all()
#     return render(request, 'index.html', {'news': news,
#                                           'newsImg':newsImg,
#                                           'newsEcnom':newsEcnom,
#                                           'newsCriminal': newsCriminal,
#                                           'newsSport': newsSport
#                                           })


def economic_list(request):
    news = Post.objects.filter(category=2)
    return render(request, 'detail.html', {'news': news})


def all_view(request, id):
    my_object = get_object_or_404(Post, id=id)

    # Увеличение счетчика просмотров
    my_object.hit_count_generic.hit()
    return render(request, 'views.html', {'my_object': my_object})


def news_detail(request, id):
    news = Post.objects.get(id=id)
    return render(request, 'detail.html', {'news': news})


# class NewsDetailView(DetailView):
#     model = News
#     template_name = "detail_news.html"
#     slug_field = "slug"


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



