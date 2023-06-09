from django.urls import path, include
from .views import *


urlpatterns = [
    path('', posts),
    path('blog/search/', search),
    #
    # path('detail/<int:id>', news_detail),
    path('economic/all', economic_list),
    path('news/all', news_list),
    path('sport/all', sport_list),
    path('criminal/all', criminal_list),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('release/all/', release_list),


]