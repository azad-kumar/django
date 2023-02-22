from django.shortcuts import render
from .import models
from django.http import HttpResponse,JsonResponse
import json


# Create your views here.


def home_page(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def blog(request):
    return render(request, 'blog.html')

def contributor(request):
    return render(request, 'contributors.html')

def search(request):
    return render(request, 'search.html')

def search_result(request):
    return models.call_search_result(request)

def trending(request):
    return models.call_trending(request)

def get_keyword_properties(request):
    return models.call_get_properties(request)

def about(request):
    return render(request, 'aboutus.html')

def privacy_policy(request):
    return render(request, 'privacypolicy.html')

