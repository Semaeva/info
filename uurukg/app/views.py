from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db.models import Q
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType


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
    for i in data:
        persons = Govno.objects.filter(Q(name=i) | Q(position=i))
        return render(request, 'search_result.html', {'person': persons})


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


def get_page_views(url):
    content_type = ContentType.objects.get_for_model(PageView)
    page_views_count = PageView.objects.filter(
        content_type=content_type,
        object_id=url,
    ).count()
    return page_views_count


def count_view():
    page_url = "/my-page/"
    views_count = get_page_views(page_url)
    print(f"Количество просмотров страницы {page_url}: {views_count}")