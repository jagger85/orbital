from django.shortcuts import render
from django.contrib import messages
from django.views import View
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_headers

# Page views and htmx middleware


@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
@method_decorator(vary_on_headers('HX-Request'), name='dispatch')
class HTMXView(View):
    """
    Generic view handler for HTMX requests

    This handler is needed to correctly send the views when 
    the user reloads the page or when is triggered by an htmx element

    - When the user refreshes the browser we need to send the whole page 

    - When is triggered by a HTMX navigation link we only need to send the partial

    """
    template_base = None

    def get(self, request, *args, **kwargs):
        context = kwargs.get('context', {})
        context['partial_template'] = f"ui/partials/{self.template_base}.html"
        template = f"ui/partials/{self.template_base}.html" if request.htmx else "ui/main-layout.html"
        return render(request, template, context)


class OverviewView(HTMXView):
    template_base = 'overview'


class ScrapersView(HTMXView):
    template_base = 'scrapers'


class AutomationView(HTMXView):
    template_base = 'automation'


class HistoryView(HTMXView):
    template_base = 'history'


class UserManagementView(HTMXView):
    template_base = 'user-management'

    def get(self, request, *args, **kwargs):
        users = [
            {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
            {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
            {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
            {'username': 'andy', 'role': 'admin', 'email': 'andy@gmail.com'},
        ]
        context = {'users': users}
        return super().get(request, context=context)

    def post(self, request, *args, **kwargs):
        new_user = {
            'username': request.POST['username'],
            'role': request.POST['role'],
            'email': request.POST['email']
        }
        messages.success(request, 'the user has been added')
        return self.get(request)


class SettingsView(HTMXView):
    template_base = 'settings'
