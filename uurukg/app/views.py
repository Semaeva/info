from django.shortcuts import render
from .models import *


def news_list(request):
    news = News.objects.order_by('-id')[:5]
    newsImg = NewsImage.objects.all()
    newsTop = News.objects.all()
    newsEcnom = News.objects.filter(category= 1 ).all()
    return render(request, 'index.html', {'news': news, 'newsImg':newsImg, 'newsEcnom':newsEcnom })
