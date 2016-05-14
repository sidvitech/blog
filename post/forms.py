from django import forms
from django.contrib.auth.models import User
from post.models import Post, MyComment, Contact


class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ['user', 'blog_name','title', 'image', 'author', 'body']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
		}


class MyCommentForm(forms.ModelForm):
	
	class Meta:
		model = MyComment
		fields = ['title',]
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
		}

class UserDeleteComment(forms.ModelForm):
	class Meta:
		model = MyComment
		fields = ['title']
		widgets = {
			'title': forms.TextInput(attrs={ 'required': 'required' }),
	}


class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
	required=True,
	widget=forms.Textarea
	)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "What do you want to say?"