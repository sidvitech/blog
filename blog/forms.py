from django import forms
from django.contrib.auth.models import User
from blog.models import UserProfile, Posts, Category
from datetime import datetime, date
from project import settings


class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=User
		fields=('username', 'password', 'email', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields=('profession','birthdate','lives_in','profile_picture')


class CategoryForm(forms.ModelForm):
	name=forms.CharField(max_length=128, help_text="Please enter the category name")
	total_posts=forms.IntegerField(initial=0)
	class Meta:
		model=Category
		fields=('name',)


class PostsForm(forms.ModelForm):
	title=forms.CharField(max_length=100)
	details = forms.CharField(widget=forms.Textarea)
	thumb=forms.ImageField(widget=forms.ImageField)
	category=forms.CharField(max_length=100)
	likes=forms.IntegerField(initial=0)
	views=forms.IntegerField(initial=0)
	stars=forms.IntegerField(initial=0)

	class Meta:
		model=Posts	
		fields=('title',)
	


