from django import forms
from django.contrib.auth.models import User
from userblog.models import Blog


class BlogForm(forms.ModelForm):
	
	class Meta:
		model = Blog
		fields = ['blog_name', 'developer_name', 'category']
		widgets = {
			'blog_name': forms.TextInput(attrs={ 'required': 'required' }),
		}

	def clean_name(self):
		blog_name = self.cleaned_data['blog_name']
		try:
			Blog.objects.get(blog_name=blog_name)
		except Blog.DoesNotExist:
			return blog_name
		raise forms.ValidationError("That username is already taken, please select another name")

class UserDeleteBlog(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['blog_name']
		widgets = {
			'blog_name': forms.TextInput(attrs={ 'required': 'required' }),
	}