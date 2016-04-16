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
		fields = ('user','blogname','postname','text','visibility','picture','video')

class CommentAddForm(ModelForm):
	class Meta:
		model = CommentAdd
		fields = ('comment',)

class CommentEditForm(ModelForm):
	# username = forms.CharField(label=(u'User Name of Post'))
	# postname = forms.CharField(label=(u'Post name'))
	class Meta:
		model = CommentAdd
		fields = ('postname','comment')
		# exclude = ('postname',)		

	def clean_comment(self):
			comment = self.cleaned_data['comment']
					
	def clean_postname(self):
			postname = self.cleaned_data['postname']			
