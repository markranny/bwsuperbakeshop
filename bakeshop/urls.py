# bakeshop/urls.py

from django.urls import path
from . import views

app_name = 'bakeshop'

urlpatterns = [
    # Main pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('franchise/', views.franchise, name='franchise'),
    path('career/', views.career, name='career'),
    path('location/', views.location, name='location'),
    
    # Menu category and detail pages
    path('menu/category/<slug:category_slug>/', views.menu_category, name='menu_category'),
    path('menu/special-offers/', views.special_offers, name='special_offers'),
    
    # Job listings and applications
    path('career/jobs/', views.job_listings, name='job_listings'),
    path('career/job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('career/apply/<int:job_id>/', views.job_apply, name='job_apply'),
    
    # Location details
    path('location/<int:location_id>/', views.location_detail, name='location_detail'),
    path('location/search/', views.location_search, name='location_search'),
    
    # Franchise request
    path('franchise/request/', views.franchise_request, name='franchise_request'),
    
    # Contact forms
    path('contact/', views.contact, name='contact'),
    path('contact/thank-you/', views.contact_thank_you, name='contact_thank_you'),
]