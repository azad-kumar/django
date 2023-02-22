from django.urls import path
from . import views



urlpatterns = [
    path('', views.search, name='home_page'),
    path('team', views.team, name='team'),
    path('blog', views.blog, name='blog'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('contributor', views.contributor, name='contributor'),
    path('search-result', views.search_result, name='searchresult'),
    path('search', views.search, name='search'),
    path('trending',views.trending, name='trending'),
    path('contact',views.home_page, name='trending'),
    path('get-keyword-properties', views.get_keyword_properties, name='get_keyword_properites'),
    path('about',views.about, name='about'),
    path('privacy-policy',views.privacy_policy, name='privacy'),
]
