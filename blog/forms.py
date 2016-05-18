from django import forms
from django.contrib.auth.models import User
from blog.models import UserProfile, Posts, Category
from datetime import datetime, date

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	email=forms.EmailField()
	class Meta:
		model=User
		fields=('username', 'password', 'email', 'first_name', 'last_name')
		
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken, please select another name")



class UserProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('profile_picture',)


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
        
	
		

