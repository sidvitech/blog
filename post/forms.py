from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from blogapp.models import Blogapp
from post.models import PostAdd, CommentAdd


class PostAddForm(ModelForm):
	visibility_1='public'
	visibility_2 = 'private'
	visibility_choices = (
		(visibility_1,u"Public"),
		(visibility_2,u"Private")
		)
	visibility  = forms.ChoiceField(choices=visibility_choices)

	choice_1 = 'text'
	choice_2 = 'image'
	choicess = (
		(choice_1,u"Text"),
		(choice_2,u"Image")
		)
	choice = forms.ChoiceField(choices = choicess)
	class Meta:
		model = PostAdd
		fields = ('blogname','postname','choice','text','visibility','picture')

class CommentAddForm(ModelForm):
	class Meta:
		model = CommentAdd
		fields = ('postname','comment')