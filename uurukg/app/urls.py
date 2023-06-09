from django.urls import path, include
from .views import *


urlpatterns = [
    path('', posts),
    path('blog/search/', search),

    path('detail/<int:id>', news_detail),
    path('economic/all', economic_list),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),


    # path('views/<int:id>', all_view),
    # path('top/all', top_list),
    # path('econom/<int:id>', news_detail),
    # path('econom/<int:id>', news_detail),
    # path('econom/<int:id>', news_detail),
    # path("blog/", posts),

    # path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

    # path('<slug>', PostDetailView.as_view(), name='post'),

    # path('blog/<int:pk>/', PostDetailView.as_view(), name='post'),
    # path('<slug:slug>/',PostDetailView.as_view().index)
    # path('club/<int:pk>', schedule_list),
]