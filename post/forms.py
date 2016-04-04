from django import forms
from django.contrib.auth.models import User
from post.models import Post, MyComment


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['blog_name','title', 'date_created', 'tag', 'body']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
		}


class MyCommentForm(forms.ModelForm):
	
	class Meta:
		model = MyComment
		fields = ['post_name', 'title']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
		}