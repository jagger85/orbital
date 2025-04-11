from django import template
from .icons import ICONS  

register = template.Library()

sidebar = {
    'logo': '',
    'elements': [
        {
            'label': 'Overview',
            'path': '/',
            'icon': ICONS['house'],  
            'roles': '',
        },
        {
            'label': 'Run Scraper',
            'path': '/scrap',
            'icon': ICONS['download'],  
            'roles': '',
        },
        {
            'label': 'Scheduled Tasks',
            'path': '/automation',
            'icon': ICONS['settings'],  
            'roles': '',
        },
        {
            'label': 'Scraping History',
            'path': '/history',
            'icon': ICONS['file'],  
            'roles': '',
        },
        {
            'label': 'Manage Users',
            'path': '/user-management',
            'icon': ICONS['user'],  
            'roles': '',
        },
        {
            'label': 'Preferences',
            'path': '/preferences',
            'icon': ICONS['info'],  
            'roles': '',
        },
    ],
    'footer_text': 'lorem ipsum'
}

@register.simple_tag
def get_sidebar():
    return sidebar