from django import forms
from django.contrib.auth.models import User
from category.models import Category


class UserCategoryForm(forms.ModelForm):
	
	class Meta:
		model = Category
		fields = ['category_name', 'user_name']
		widgets = {
			'category_name': forms.TextInput(attrs={ 'required': 'required' }),
		}

	def clean_name(self):
		category_name = self.cleaned_data['category_name']
		try:
			Category.objects.get(name=category_name)
		except Category.DoesNotExist:
			return category_name
		raise forms.ValidationError("That username is already taken, please select another name")
