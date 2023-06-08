from django.urls import path, include
from .views import *


urlpatterns = [
    path('', news_list),
    path('blog/search/', search),

    path('econom/', economic_list),
    path("blog/", posts),
    # path('<slug>', NewsDetailView.as_view(), name="news"),
    # path('<slug>', PostDetailView.as_view(), name='post'),
     path('post/<slug>', PostDetailView.as_view(), name='post'),
    # path('blog/<int:pk>/', PostDetailView.as_view(), name='post'),
    # path('<slug:slug>/',PostDetailView.as_view().index)
    # path('club/<int:pk>', schedule_list),
]