from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class News(ListView):
    model = Post
    # ordering = '-time_in'
    queryset = Post.objects.order_by('-time_in')
    template_name = 'news.html'
    context_object_name = 'news'


class New(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

# Create your views here.
