# users/urls.py
from . import views
from django.urls import path
from .views import register, user_login, user_logout

app_name='users'

urlpatterns = [
    path('register/', register, name='register'),
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
