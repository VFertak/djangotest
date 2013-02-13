from django.conf.urls import patterns, url
from swissmap import views

urlpatterns = patterns('',
   url(r'^$', views.index, name='index'),
)