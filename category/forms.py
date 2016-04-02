from django import forms
from django.contrib.auth.models import User
from category.models import Category


class UserCategoryForm(forms.ModelForm):
	
	class Meta:
		model = Category
		fields = ['user_register_name', 'name', 'user_name']
		widgets = {
			'name': forms.TextInput(attrs={ 'required': 'required' }),
		}

	def clean_name(self):
		name = self.cleaned_data['name']
		try:
			Category.objects.get(name=name)
		except Category.DoesNotExist:
			return name
		raise forms.ValidationError("That username is already taken, please select another name")

class UserDeleteCategory(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={ 'required': 'required' }),
	}