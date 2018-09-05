from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.tasks_list, name='tasks_list'),
    url(r'^todo/new/$', views.add_new_item, name='add_new'),
]