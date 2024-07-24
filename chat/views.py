# <!-- chat/views.py -->

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


def lobby(request):
    context = {'current_page': 'lobby'}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['users'] = User.objects.all()
    else:
        context['username'] = 'Anonymous'

    room_name = request.GET.get('room_name')
    if room_name:
        context['room_name'] = room_name
        return render(request, 'chat/lobby.html', context)
    
    user_select = request.GET.get('user_select')
    private_chat_room = request.GET.get('private_chat_room')
    if user_select and private_chat_room:
        return redirect(f'/chat/?room_name={private_chat_room}')

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

