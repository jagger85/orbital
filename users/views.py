from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.


class LoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('overview')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('overview')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(LogoutView):
    next_page = 'login'


class PasswordChangeView(PasswordChangeView):
    def form_valid(self, form):
        return super().form_valid(form)

class PasswordChangeDoneView(PasswordChangeDoneView):
    pass