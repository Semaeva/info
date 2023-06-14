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
    # path('opg/all', opg_list),
    path('sng/all', sng_list),
    path('departments/all', department_list),
    path('analitika/all', analitika_list),

    path('press_release/<int:id>/', release_list),

    path('post/<int:pk>/', PostDetailView.as_view(), name='posts-detail'),
    path('dopinfo/<int:pk>/', GovnoDetailView.as_view(), name='dopinfo-detail'),
    path('sng/<int:pk>/', SngDetailView.as_view(), name='sng-detail'),
    path('release/<int:pk>/', ReleaseDetailView.as_view(), name='realese-detail'),


]