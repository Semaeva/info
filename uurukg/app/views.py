from datetime import timedelta

import hitcount.models
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.crypto import get_random_string
from hitcount.models import Hit
from django.core.paginator import Paginator, Page

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


def recent_record():
    current_time = datetime.now()
    half_hour_ago = current_time - timedelta(minutes=30)
    recent_records = AnonymousUserCount.objects.filter(created_date__gte=half_hour_ago).count()
    return recent_records


def get_connections(ip):
    anonymous_user_count, created = AnonymousUserCount.objects.get_or_create(ip_address=ip)
    anonymous_user_count.session_key = get_random_string(32)
    anonymous_user_count.save()


def posts(request):
    posts = Post.objects.all()[:6]
    newsEcnom = Post.objects.filter(category=2).all()[:3]
    newsSport = Post.objects.filter(category=3).all()[:3]
    newsCriminal = Post.objects.filter(category=1).all()[:3]
    newsTop = Post.objects.filter(top_news=True).all()[:3]
    sng = NewsSNG.objects.all()[:3]
    get_connections(request.META.get('REMOTE_ADDR'))
    return render(request, "index.html", {'posts': posts,
                                          'newsEconom': newsEcnom,
                                          'newsSport': newsSport,
                                          'newsCriminal': newsCriminal,
                                          'top': newsTop,
                                          'sng': sng,
                                          'anonym': recent_record()
                                       })


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'detail.html'
    count_hit = True


class SngDetailView(HitCountDetailView):
    model = NewsSNG
    template_name = 'sng_detail.html'
    count_hit = True


class ReleaseDetailView(HitCountDetailView):
    model = Press_release
    template_name = 'release_detail.html'
    count_hit = True


class GovnoDetailView(HitCountDetailView):
    model = Govno
    template_name = 'dopinfo.html'
    count_hit = True


def release_list(request):
    news = Press_release.objects.all()
    return render(request, 'release.html', {'news': news})


def economic_list(request):
    news = Post.objects.filter(category=2)
    return render(request, 'econom.html', {'news': news})


def sng_list(request):
    news = NewsSNG.objects.all()
    return render(request, 'sng.html', {'news': news})


def criminal_list(request):
    news = Post.objects.filter(category=1)
    return render(request, 'criminal.html', {'news': news})


def sport_list(request):
    news = Post.objects.filter(category=3)
    return render(request, 'sport.html', {'news': news})


def repoter_list(request):
    news = Post.objects.filter(category=7)
    return render(request, 'reporter.html', {'news': news})


def analitika_list(request):
    news = Post.objects.filter(category=4)
    return render(request, 'analitika.html', {'news': news})


def news_list(request, page_number=1):
    news = Post.objects.all()
    paginated  = Paginator(news, 9)
    page_number = request.GET.get('page')
    page = paginated.get_page(page_number)
    return render(request, 'all_news.html', {'news': page })


def opg_list(request):
    news = Post.objects.filter(category=6)
    return render(request, 'opg.html', {'news': news})


def korrupcia_list(request):
    news = Post.objects.filter(category=5)
    return render(request, 'korrupcia.html', {'news': news})


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


def count_anonim(request):
    print(f'запрос {request}')
    return render(request, 'index_.html', {'test':0})
    # ip_address = request.META.get('REMOTE_ADDR')
    # print(f'Ip address {ip_address}')
    # anonymous_user_count, created = AnonymousUserCount.objects.get_or_create(ip_address=ip_address)
    # anonymous_user_count.session_key = get_random_string(32)
    # anonymous_user_count.save()
    #
    # HitCountMixin.hit_count(request, anonymous_user_count)

    # return render(request, 'count.html', {'anonymous_user_count': anonymous_user_count})



