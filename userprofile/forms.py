from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from datetime import datetime, date


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields=('designation','birthdate','lives_in','profile_picture')

class EditProfileForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name') 
    email = forms.CharField(label='Email') 

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']