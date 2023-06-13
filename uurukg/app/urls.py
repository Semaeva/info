from django.urls import path, include
from .views import *


urlpatterns = [
    path('', posts),
    path('blog/search/', search),

    path('economic/all', economic_list),
    path('news/all', news_list),
    path('sport/all', sport_list),
    path('criminal/all', criminal_list),
    path('reporter/all', repoter_list),
    path('korrupcia/all', korrupcia_list),
    path('opg/all', opg_list),
    path('sng/all', sng_list),
    path('analitika/all', analitika_list),
    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('dopinfo/<int:pk>/', GovnoDetailView.as_view(), name='dopinfo-detail'),
    path('sng/<int:pk>/', SngDetailView.as_view(), name='sng-detail'),
    path('release/<int:pk>/', ReleaseDetailView.as_view(), name='realese-detail'),
    # path('news/post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('release/all/', release_list),



    # path('', count_anonim),



]