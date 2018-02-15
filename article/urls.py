from django.urls import re_path

from . import views

app_name = 'article'

urlpatterns = [
    re_path(r'articles/get/(?P<article_id>\d+)/$', views.article, name="article"),
    re_path(r'^$', views.articles, name='articles'),
]
