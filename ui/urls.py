from django.urls import path
from . import views

urlpatterns = [
    
    # Pages
    path('', views.overview, name='overview' ),
    path('scrap/', views.scrapers ),
    path('automation/', views.automation ),
    path('history/', views.history ),
    path('user-management/', views.user_management ),
    path('preferences/', views.settings ),
]