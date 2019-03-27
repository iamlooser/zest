from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from zest2k19 import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^$', views.base),
    url(r'^index/$', views.index),
]

from django.conf import settings
from django.conf.urls.static import static


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
