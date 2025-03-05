from django.urls import path
from .views import list_blog, detail_blog, blog_authors

urlpatterns = [
    path("list/", list_blog, name='list_blog'),
    path("detail/<int:blog_id>", detail_blog, name='detail_blog'),
    path("blog-author", blog_authors, name='author_blog'),
]