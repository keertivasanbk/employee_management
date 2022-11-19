from django import forms
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')


class UserProfileInfo(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('employe_role','dob','phone_number','qrcode')


