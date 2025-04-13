from django.urls import path
from .views import OverviewView, ScrapersView, AutomationView, HistoryView, UserManagementView, SettingsView

urlpatterns = [
    
    # Pages
    path('', OverviewView.as_view(), name='overview' ),
    path('scrap/', ScrapersView.as_view(), name='scrap' ),
    path('automation/', AutomationView.as_view(), name='automation' ),
    path('history/', HistoryView.as_view(), name='history' ),
    path('user-management/', UserManagementView.as_view(), name='user-management' ),
    path('preferences/', SettingsView.as_view(),name='settings' ),
]