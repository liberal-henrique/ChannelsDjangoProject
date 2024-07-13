# <!-- chat/views.py -->

from django.shortcuts import render, redirect

# Create your views here.

def lobby(request):
    context = {'current_page': 'lobby'}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    else:
        context['username'] = 'Anonymous'
    return render(request, 'chat/lobby.html', context)
#

def login(request):
    context = {'current_page': 'login_strait'}
    if request.user.is_authenticated:
        context['username'] = request.user.username
    else:
        context['username'] = 'Anonymous'
    #
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            return redirect(f'/chat/?room_name={room_name}')
        #
    #
    return render(request, 'chat/login.html', context)
            
#

