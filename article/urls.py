from django.urls import re_path

from . import views

app_name = 'article_app'

urlpatterns = [
    re_path(r'articles/get/(?P<article_id>\d+)/$', views.article, name="article"),
    re_path(r'^$', views.articles, name='articles'),
    re_path(r'articles/add_like/(?P<article_id>\d+)/$', views.add_like, name="add_like"),
    re_path(r'articles/add_comment/(?P<article_id>\d+)/$', views.add_comment, name="add_comment"),
]
