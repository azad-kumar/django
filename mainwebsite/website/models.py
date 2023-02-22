from django.db import models
from . import main
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your models here.


def call_search_result(request):
    request_keyword = request.GET['keyword']
    redbubble_obj = main.keyword(request_keyword)
    google_obj=main.google(request_keyword)
    keyword_properties_obj=main.keyword_properties()
    design_count, keywords = redbubble_obj.get_keywords_and_design_count()
    google=google_obj.get_response_json()
    trending=redbubble_obj.get_keyword_trend_request()
    keyword_with_properties=keyword_properties_obj.get_dict_with_properties(keywords[:5])
    after_five=keywords[5:]
    return render(request, 'searchresult.html',{'keyword':keyword_with_properties,'Google':google,'trending_searches':trending,'main_keyword':request_keyword,'design_count':design_count,'data':after_five})


def call_trending(request):
    trend_obj = main.get_trending()
    trending_keywords = trend_obj.get_trending_keywords()
    popular_searches = trend_obj.get_popular_searches()
    popular_artist = trend_obj.get_popular_artist()
    fan_art_properties = trend_obj.get_fan_art_properties()
    return render(request, 'trending.html', {'trending_keywords': trending_keywords, 'popular_searches': popular_searches, 'popular_artist': popular_artist, 'fan_art_properties': fan_art_properties})


def call_get_properties(request):
    keyword_list=[]
    data = {}
    keyword_list =request.GET.getlist('list_data', [])
    get_properties_obj=main.keyword_properties()
    data=get_properties_obj.get_dict_with_properties(keyword_list)
    return JsonResponse(data)
