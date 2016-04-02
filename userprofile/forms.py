from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from userprofile.models import userprof, profilepic, UserProfile

class userprofForm(ModelForm):
	class Meta:
		model = userprof
		fields = ('fname','lname','mobileno','gender','emailid')

class profilepicForm(ModelForm):
	class Meta:
		model = profilepic
		fields = ('picture',)

class UserForm(ModelForm):
	# username = forms.CharField(label=(u'User Name'))
	
	# mobileno=forms.IntegerField(label=(u'Mobile No'))
	# gender= forms.CharField(label=(u'Gender'))
	# email = forms.EmailField(label=(u'Email Address'))
	# first_name=forms.CharField(label=(u'First Name'))
	# last_name=forms.CharField(label=(u'Last Name'))
	# mobileno=forms.IntegerField(label=(u'Mobile No'))
	
	class Meta:
		model=User
		fields =('username','email','first_name','last_name')
		# exclude =('user1',)

	def clean_username(self):
			username = self.cleaned_data['username']
			try:
					User.objects.get(username=username)
			except User.DoesNotExist:
					return username
			raise forms.ValidationError("That username is already taken please select another.")

class UserForm1(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields =('mobileno','gender','picture')

class UpdatepicForm(forms.ModelForm):
	username = forms.CharField(label=(u'User Name'))
	class Meta:
		model = UserProfile
		fields =('picture',)
