from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'requied': 'required'}))
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'required': 'required'}))

	class Meta:
		model = User
		fields = ['username', 'email']
		widgets = {
			'username': forms.TextInput(attrs={ 'required': 'required' }),
		}

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken, please select another name")

	def clean(self):
		cleaned_data = super(UserRegistrationForm, self).clean()
		if cleaned_data['password1'] != cleaned_data['password2']:
			raise forms.ValidationError("The Password did not match. Please try again")
		return cleaned_data

class UserLoginForm(forms.Form):
	username = forms.CharField(label=(u'User Name'))
	password = forms.CharField(label=(u'Password'), 
			widget=forms.PasswordInput(render_value=False)
		)
	
class UserPasswordResetForm(forms.Form):
	username = forms.CharField(label=(u'User Name'))
	password1 = forms.CharField(label="Old Password", widget=forms.PasswordInput(attrs={'requied': 'required'}))
	password2 = forms.CharField(label="New Password", widget=forms.PasswordInput(attrs={'required': 'required'}))
