from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls"), name='polls'),
    path("admin/", admin.site.urls, name='admin'),
    path("blog/", include("blog.urls"), name='blog'),
]