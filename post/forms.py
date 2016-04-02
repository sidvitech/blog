from django import forms
from django.contrib.auth.models import User
from post.models import Post


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['blog_name','title', 'date_created']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
		}
