from django.urls import re_path

from . import views

app_name = 'article'

urlpatterns = [
    re_path(r'^1/', views.basic_one),
    re_path(r'^2/', views.template_two),
    re_path(r'^3/', views.template_three_simple),
    re_path(r'^articles/all/$', views.articles),
    re_path(r'articles/get/(?P<article_id>\d+)/$', views.article),
    re_path(r'^$', views.articles),
]
