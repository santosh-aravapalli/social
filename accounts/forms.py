from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms



class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','email']



class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['gender','age','date_of_birth']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

