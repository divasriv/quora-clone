from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.generic import FormView,RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin,ListView
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterView(FormView):
    ''' View for user registration. '''
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Registration successful! You can now log in.")
        return super().form_valid(form)

class LoginView(FormView):
    ''' View for user login. '''
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            login(self.request, user)
        return super().form_valid(form)

class LogoutView(RedirectView):
    ''' View for user logout. '''
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class HomeView(LoginRequiredMixin, ListView):
    ''' View for the home page displaying questions. '''
    template_name = 'home.html'
