from django.shortcuts import render
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import RegisterUserForm, LoginUserForm 
from taskmanager.settings import base

# Create your views here.

def logoutUser(request):
    logout(request)
    return redirect(base.LOGIN_REDIRECT_URL)

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'auth/login.html'


