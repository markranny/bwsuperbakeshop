# dashboard/urls.py

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard home
    path('', views.dashboard_home, name='home'),
    
    # Content management for each page
    path('home/', views.manage_home, name='manage_home'),
    path('about/', views.manage_about, name='manage_about'),
    path('menu/', views.manage_menu, name='manage_menu'),
    path('career/', views.manage_career, name='manage_career'),
    path('franchise/', views.manage_franchise, name='manage_franchise'),
    path('location/', views.manage_location, name='manage_location'),
    
    # CRUD operations for specific models
    
    # Home page management
    path('home/banner/add/', views.home_banner_add, name='home_banner_add'),
    path('home/banner/edit/<int:banner_id>/', views.home_banner_edit, name='home_banner_edit'),
    path('home/banner/delete/<int:banner_id>/', views.home_banner_delete, name='home_banner_delete'),
    
    path('home/section/edit/<int:section_id>/', views.home_section_edit, name='home_section_edit'),
    
    # About page management
    path('about/section/edit/<int:section_id>/', views.about_section_edit, name='about_section_edit'),
    
    path('about/team/add/', views.team_member_add, name='team_member_add'),
    path('about/team/edit/<int:member_id>/', views.team_member_edit, name='team_member_edit'),
    path('about/team/delete/<int:member_id>/', views.team_member_delete, name='team_member_delete'),
    
    path('about/award/add/', views.award_add, name='award_add'),
    path('about/award/edit/<int:award_id>/', views.award_edit, name='award_edit'),
    path('about/award/delete/<int:award_id>/', views.award_delete, name='award_delete'),
    
    path('about/timeline/add/', views.timeline_add, name='timeline_add'),
    path('about/timeline/edit/<int:timeline_id>/', views.timeline_edit, name='timeline_edit'),
    path('about/timeline/delete/<int:timeline_id>/', views.timeline_delete, name='timeline_delete'),
    
    # Menu page management
    path('menu/category/add/', views.menu_category_add, name='menu_category_add'),
    path('menu/category/edit/<int:category_id>/', views.menu_category_edit, name='menu_category_edit'),
    path('menu/category/delete/<int:category_id>/', views.menu_category_delete, name='menu_category_delete'),
    
    path('menu/item/add/', views.menu_item_add, name='menu_item_add'),
    path('menu/item/edit/<int:item_id>/', views.menu_item_edit, name='menu_item_edit'),
    path('menu/item/delete/<int:item_id>/', views.menu_item_delete, name='menu_item_delete'),
    
    path('menu/featured/add/', views.featured_item_add, name='featured_item_add'),
    path('menu/featured/edit/<int:featured_id>/', views.featured_item_edit, name='featured_item_edit'),
    path('menu/featured/delete/<int:featured_id>/', views.featured_item_delete, name='featured_item_delete'),
    
    path('menu/offer/add/', views.special_offer_add, name='special_offer_add'),
    path('menu/offer/edit/<int:offer_id>/', views.special_offer_edit, name='special_offer_edit'),
    path('menu/offer/delete/<int:offer_id>/', views.special_offer_delete, name='special_offer_delete'),
    
    # Career page management
    path('career/section/edit/<int:section_id>/', views.career_section_edit, name='career_section_edit'),
    
    path('career/category/add/', views.job_category_add, name='job_category_add'),
    path('career/category/edit/<int:category_id>/', views.job_category_edit, name='job_category_edit'),
    path('career/category/delete/<int:category_id>/', views.job_category_delete, name='job_category_delete'),
    
    path('career/position/add/', views.job_position_add, name='job_position_add'),
    path('career/position/edit/<int:position_id>/', views.job_position_edit, name='job_position_edit'),
    path('career/position/delete/<int:position_id>/', views.job_position_delete, name='job_position_delete'),
    
    path('career/testimonial/add/', views.employee_testimonial_add, name='employee_testimonial_add'),
    path('career/testimonial/edit/<int:testimonial_id>/', views.employee_testimonial_edit, name='employee_testimonial_edit'),
    path('career/testimonial/delete/<int:testimonial_id>/', views.employee_testimonial_delete, name='employee_testimonial_delete'),
    
    path('career/benefit/add/', views.benefit_add, name='benefit_add'),
    path('career/benefit/edit/<int:benefit_id>/', views.benefit_edit, name='benefit_edit'),
    path('career/benefit/delete/<int:benefit_id>/', views.benefit_delete, name='benefit_delete'),
    
    # Franchise page management
    path('franchise/section/edit/<int:section_id>/', views.franchise_section_edit, name='franchise_section_edit'),
    
    path('franchise/model/add/', views.franchise_model_add, name='franchise_model_add'),
    path('franchise/model/edit/<int:model_id>/', views.franchise_model_edit, name='franchise_model_edit'),
    path('franchise/model/delete/<int:model_id>/', views.franchise_model_delete, name='franchise_model_delete'),
    
    path('franchise/testimonial/add/', views.franchisee_testimonial_add, name='franchisee_testimonial_add'),
    path('franchise/testimonial/edit/<int:testimonial_id>/', views.franchisee_testimonial_edit, name='franchisee_testimonial_edit'),
    path('franchise/testimonial/delete/<int:testimonial_id>/', views.franchisee_testimonial_delete, name='franchisee_testimonial_delete'),
    
    path('franchise/faq/add/', views.faq_add, name='faq_add'),
    path('franchise/faq/edit/<int:faq_id>/', views.faq_edit, name='faq_edit'),
    path('franchise/faq/delete/<int:faq_id>/', views.faq_delete, name='faq_delete'),
    
    path('franchise/investment/add/', views.investment_breakdown_add, name='investment_breakdown_add'),
    path('franchise/investment/edit/<int:item_id>/', views.investment_breakdown_edit, name='investment_breakdown_edit'),
    path('franchise/investment/delete/<int:item_id>/', views.investment_breakdown_delete, name='investment_breakdown_delete'),
    
    # Location page management
    path('location/add/', views.store_location_add, name='store_location_add'),
    path('location/edit/<int:location_id>/', views.store_location_edit, name='store_location_edit'),
    path('location/delete/<int:location_id>/', views.store_location_delete, name='store_location_delete'),
    
    path('location/stat/add/', views.location_stat_add, name='location_stat_add'),
    path('location/stat/edit/<int:stat_id>/', views.location_stat_edit, name='location_stat_edit'),
    path('location/stat/delete/<int:stat_id>/', views.location_stat_delete, name='location_stat_delete'),
    
    # Process steps management (shared between career and franchise)
    path('process/add/', views.process_step_add, name='process_step_add'),
    path('process/edit/<int:step_id>/', views.process_step_edit, name='process_step_edit'),
    path('process/delete/<int:step_id>/', views.process_step_delete, name='process_step_delete'),
    
    # Gallery management
    path('gallery/add/', views.gallery_image_add, name='gallery_image_add'),
    path('gallery/edit/<int:image_id>/', views.gallery_image_edit, name='gallery_image_edit'),
    path('gallery/delete/<int:image_id>/', views.gallery_image_delete, name='gallery_image_delete'),
    
    # Contact messages management
    path('messages/', views.contact_messages, name='contact_messages'),
    path('messages/<int:message_id>/', views.contact_message_detail, name='contact_message_detail'),
    path('messages/mark-as-read/<int:message_id>/', views.mark_message_as_read, name='mark_message_as_read'),
    path('messages/delete/<int:message_id>/', views.contact_message_delete, name='contact_message_delete'),
    
    # Site settings
    path('settings/', views.site_settings, name='site_settings'),
]