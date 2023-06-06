from django.urls import path, include
from .views import *


urlpatterns = [
    path('', news_list),
    path('search/', search),

    path('blog/', blog),
    path('<slug>', PostDetailView.as_view(), name='post'),

]