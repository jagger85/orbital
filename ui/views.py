from django.shortcuts import render

def htmx_view(request, template_base):
    """
    Generic view handler for HTMX requests
    
    This handler is needed to correctly send the views when 
    the user reloads the page or when is triggered by an htmx element
    
    - When the user refreshes the browser we need to send the whole page 

    - When is triggered by a HTMX navigation link we only need to send the partial

    """

    context = {
        'partial_template': f"ui/partials/{template_base}.html"
    }
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
    return htmx_view(request, 'user-management')


def settings(request):
    return htmx_view(request, 'settings')
