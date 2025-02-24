from django.urls import path
from .views import home_redirect,property_list, property_detail, create_new_property, update_existing_property,patch_property,delete_property
from . import views

urlpatterns = [
    path("", home_redirect, name="home_redirect"), 
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:pk>/', views.property_detail, name='property_detail'),
    path('create_new_property/', create_new_property, name='create_new_property'),
    path('update_existing_property/<int:pk>/', update_existing_property, name='update_existing_property'),
    path('patch_property/<int:pk>/', patch_property, name='patch_property'),
    path('delete_property/<int:pk>/', delete_property, name='delete_property'), 
]
