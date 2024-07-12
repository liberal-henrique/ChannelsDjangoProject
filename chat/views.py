from django.shortcuts import render, redirect

# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html', {
        'username': request.user.username,
    })
#

def login(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            return redirect(f'/chat/?room_name={room_name}')
    return render(request, 'chat/login.html')
            
#

