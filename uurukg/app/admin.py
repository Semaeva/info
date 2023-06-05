from django.contrib import admin
from .models import *


admin.site.site_header = 'Панель администратора UURUKG'
admin.site.index_title = 'UURUKG'

admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(Category)
admin.site.register(GovnoImage)
admin.site.register(Govno)