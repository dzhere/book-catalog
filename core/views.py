from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.urls import reverse

def index_view(request):
    return render(request, 'index.html')

def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'user/registration.html', {'form': form})

class LoginFormView(LoginView):
    redirect_field_name = 'home'
    redirect_authenticated_user = True
    template_name = 'user/login.html'

    def get_redirect_url(self):
        return reverse(self.redirect_field_name)

class LogoutFormView(LogoutView):
    next_page = 'home'