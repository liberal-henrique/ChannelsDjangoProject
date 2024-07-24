from django.urls import path, include

urlpatterns = [
    path('ws/', include('game.routing'))
]
