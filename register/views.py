from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



class Registration(CreateView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'registration.html'


class NewLoginForm(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse("home")


@login_required(login_url='sign-in')
def logout_user(request):
    logout(request)
    return redirect('home')


def sign_in(request):
    page = 'signin'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Not correct')

    return render(request, 'login.html', {'page': page})
