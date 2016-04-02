from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from blogapp.models import Blogapp
from category.models import Category


class BlogForm(ModelForm):
	visibility_1='public'
	visibility_2 = 'private'
	visibility_choices = (
		(visibility_1,u"Public"),
		(visibility_2,u"Private")
		)
	visibility  = forms.ChoiceField(choices=visibility_choices)

	class Meta:
		model = Blogapp
		fields = ('category','blogname','visibility')

# class BF(ModelForm):
# 	class Meta:
# 		model = Category
# 		fields = ('category_name',)
class DeleteBlogForm(ModelForm):
	class Meta:
		model = Blogapp
		fields = ('blogname',)

def clean_blogname(self):
			blogname = self.cleaned_data['blogname']
			try:
					Blogapp.objects.get(name=blogname)
			except Blogapp.DoesNotExist:
					return blogname
			raise forms.ValidationError("That blog is already taken please select another.")		