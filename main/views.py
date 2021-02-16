from django.shortcuts import render
from .models import Post

import json
from django.http import HttpResponse, JsonResponse
import requests
from bs4 import BeautifulSoup
from django.views import View

def index(request):
    posts = Post.objects.all().order_by('date_int')
    return render(request, 'main/index.html', {
        'posts':posts,
    })

def nike(request):
    posts = Post.objects.all().order_by('date_int')
    return render(request, 'main/nike.html', {
        'posts':posts,
    })
def converse(request):
    posts = Post.objects.all().order_by('date_int')
    return render(request, 'main/converse.html', {
        'posts':posts,
    })