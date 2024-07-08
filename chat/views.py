from django.shortcuts import render

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')
#

def login(request):
    return render(request, 'chat/login.html')
#