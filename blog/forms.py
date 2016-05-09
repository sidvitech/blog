from django import forms
from django.contrib.auth.models import User
from blog.models import UserProfile, Posts
from datetime import datetime, date

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('first_name','last_name','email')

class PostsForm(forms.ModelForm):
	title=forms.CharField(max_length=100)
	details = forms.CharField(widget=forms.Textarea)
	comments=forms.CharField(max_length=150)
	likes=forms.IntegerField(initial=0)
	views=forms.IntegerField(initial=0)
	stars=forms.IntegerField(initial=0)

	class Meta:
		model=Posts	
		fields=('title',)
        
	
		

