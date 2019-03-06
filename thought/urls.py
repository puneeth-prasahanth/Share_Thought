from django.conf.urls import  url
from . import views

urlpatterns = [
             url(r'^$', views.index,name='index'),
             url(r'^thought/(\d+)', views.thought,name='thought'),
             url(r'^comment/(\w+)/(\w+)', views.comment,name='comment'),
             #url(r'^comment/(?P<id>\w+)/(?P<topic_id>\w+)', views.comment,name='comment'),
             #url(r'^comment/(\w+)/(\w+)', views.comment,name='comment'),
               ]
