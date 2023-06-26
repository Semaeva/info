import django
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin-press-centr/', admin.site.urls),
    path('', include('app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ii8n/', include(django.conf.urls.i18n))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('pages/', include('app.urls'))
    # url(r'^ky/', include('app.urls')),
)

