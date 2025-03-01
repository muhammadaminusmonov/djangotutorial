from django.urls import path
from .views import list_blog, detail_blog

urlpatterns = [
    path("list/", list_blog, name='list_blog'),
    path("detail/<int:blog_id>", detail_blog, name='detail_blog')
]