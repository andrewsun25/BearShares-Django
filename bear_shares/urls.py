from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from bear_shares.models import Comment
from . import views

urlpatterns = [
    url(r'^list_view', ListView.as_view(queryset=Comment.objects.all().order_by("-date"))),
    url(r'^$', views.index, name='index'),
    url(r'^create_new_thread/$', views.create_new_thread, name='create_new_thread'),
]