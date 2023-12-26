"""
URL configuration for Players_Attribute_Backend project.
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.get_players_list, name='player_list'),
    path('api/countries/', views.get_country_list, name='countries_list'),
    path('api/clubs/', views.get_club_list, name='club_list'),
    path('api/attributes/', views.get_attribute_list, name='attribute_list'),
    path('api/players/<slug:slug>/', views.get_player_detail, name='player_detail'),
]