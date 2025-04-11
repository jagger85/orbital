from django.shortcuts import render
from django.contrib import messages

# Page views and htmx middleware


def htmx_view(request, template_base, context=None):
    """
    Generic view handler for HTMX requests

    This handler is needed to correctly send the views when 
    the user reloads the page or when is triggered by an htmx element

    - When the user refreshes the browser we need to send the whole page 

    - When is triggered by a HTMX navigation link we only need to send the partial

    """
    if context is None:
        context = {}

    context['partial_template'] = f"ui/partials/{template_base}.html"
    template = f"ui/partials/{template_base}.html" if request.htmx else "ui/main-layout.html"

    return render(request, template, context)


def overview(request):
    return htmx_view(request, 'overview')


def scrapers(request):
    return htmx_view(request, 'scrapers')


def automation(request):
    return htmx_view(request, 'automation')


def history(request):
    return htmx_view(request, 'history')


def user_management(request):

    users = [
        {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
        {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
        {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
        {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
    ]

    if request.method == "POST":
        new_user = {
            'username': request.POST['username'],
            'role': request.POST['role'],
            'email': request.POST['email']
        }
        messages.success(request, 'the user has been added')

    context = {
        'users': users
    }

    return htmx_view(request, 'user-management', context)


def settings(request):
    return htmx_view(request, 'settings')
