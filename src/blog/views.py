from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog


def list_blog(response):
    list = Blog.objects.all()
    return HttpResponse(f'{list}')

def detail_blog(response, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return HttpResponse(f"{blog}")