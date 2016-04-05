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
		fields = ('user','blogname','postname','text','visibility','picture')

class CommentAddForm(ModelForm):
	class Meta:
		model = CommentAdd
		fields = ('postname','comment')

class CommentEditForm(ModelForm):
	class Meta:
		model = CommentAdd
		fields = ('comment',)
		# exclude = ('postname',)		

def clean_comment(self):
			comment = self.cleaned_data['comment']
			try:
					CommentAdd.objects.get(name = comment)
			except CommentAdd.DoesNotExist:
					return comment
			raise forms.ValidationError("Enter new comment")		