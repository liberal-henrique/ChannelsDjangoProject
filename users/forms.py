from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    room_name = forms.CharField(max_length=255, required=True, label='Room Name')