from django import forms
from django.contrib.auth.models import User
from post.models import Post


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['category','title', 'image', 'body']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required', 'placeholder': 'Title' }),
		}