#<!-- users/views.py -->
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import CustomLoginForm

def register(request:HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        #
    else:
        form = UserCreationForm()
    #
    return render(request, 'users/register.html', {'form': form, 'current_page': 'register'})
#

def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            room_name = form.cleaned_data.get('room_name')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(f'/chat?room_name={room_name}')
            #
        #
    else:
        form = CustomLoginForm()
    #
    users = User.objects.all()
    return render(request, 'users/login.html', {'form': form, 'users': users, 'current_page': 'login'})
#

def user_logout(request:HttpResponse) -> HttpResponse:
    logout(request)
    return redirect('users:login')
#