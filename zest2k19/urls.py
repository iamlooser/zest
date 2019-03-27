from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from zest2k19 import views

urlpatterns = [
    url('^admin/', admin.site.urls),
    url(r'^$', views.base),
    url(r'^index/$', views.index),
]
