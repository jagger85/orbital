from django.urls import path
from . import views

urlpatterns = [
    
    # Pages
    path('', views.overview ),
    path('scrap/', views.scrapers ),
    path('automation/', views.automation ),
    path('history/', views.history ),
    path('user-management/', views.user_management ),
    path('preferences/', views.settings ),
    
    # Dialogs
    path('dialog/add-user', views.add_user, name='add-user-dialog'),
    path('dialog/add-scrap', views.add_scrap, name='add-scrap-dialog'),
    
]