from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Entry
from django.db.models import Prefetch


def list_blog(request):
    list = Blog.objects.all()
    return HttpResponse(f'{list}')

def detail_blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return HttpResponse(f"{blog}")

def blog_authors(request):
    blogs = Blog.objects.prefetch_related(Prefetch('entry_set', queryset=Entry.objects.all(), to_attr='entries'))
    context = {'blogs': blogs}
    # return render(request, 'index.html', context)