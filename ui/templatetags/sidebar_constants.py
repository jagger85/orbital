from django import template

register = template.Library()

sidebar = {
    'logo':'',
    'elements':[
    {
        'label': 'Overview',
        'path': '/',
        'icon': '',
        'roles': '',
    },
    {
        'label': 'Run Scraper',
        'path': '/scrap',
        'icon': '',
        'roles': '',
    },
    {
        'label': 'Scheduled Tasks',
        'path': '/automation',
        'icon': '',
        'roles': '',
    },
    {
        'label': 'Scraping History',
        'path': '/history',
        'icon': '',
        'roles': '',
    },
    {
        'label': 'Manage Users',
        'path': '/user-management',
        'icon': '',
        'roles': '',
    },
    {
        'label': 'Preferences',
        'path': '/preferences',
        'icon': '',
        'roles': '',
    },
],
    'footer_text':'lorem ipsum'
}

@register.simple_tag
def get_sidebar():
    return sidebar