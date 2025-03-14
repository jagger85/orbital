from django.shortcuts import render

# Page views and htmx middleware 

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

# Dialog Forms

def dialog_form_view(request, context):
    """
    Generic view handler for Dialog requests
    
    This handler is intended to reuse base-form-dialog.html

    It injects the desired form partial

    """

    return render(request, 'ui/components/dialogs/base-form-dialog.html', context)

def add_user(request):
    context = {
        'dialog_title': 'Add User',
        'request_path': '///////',
        'form_template': 'ui/components/dialogs/add-user-form.html',
    }
    return dialog_form_view(request, context)

def add_scrap(request):
    context ={
        'dialog_title': 'Add scrap',
        'request_path': '///////',
        'form_template': 'ui/components/dialogs/add-scrap-form.html'
    }
    return dialog_form_view(request, context)
