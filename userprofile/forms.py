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

	def clean_email(self):
			email = self.cleaned_data['email']  

	def clean_first_name(self):
			first_name = self.cleaned_data['first_name']

	def clean_last_name(self):
			last_name = self.cleaned_data['last_name']
					
class UserForm1(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields =('mobileno','gender','picture')

	def clean_mobileno(self):
			mobileno = self.cleaned_data['mobileno']    
			try:
				if not (mobileno.isalpha()):
					min_length=10
					max_length=13
					ph_length = str(mobileno)
					if len(ph_length) < min_length or len(ph_length) > max_length:
						raise ValidationError('Phone number length not valid')
			except (ValueError, TypeError):
				raise ValidationError('Please enter a valid phone number')
			return mobileno
				
class UpdatepicForm(forms.ModelForm):
	username = forms.CharField(label=(u'User Name'))
	class Meta:
		model = UserProfile
		fields =('picture',)

class updateprofileform(forms.ModelForm):
	username = forms.CharField(label=(u'User Name'))
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

class updateprofileform1(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields =('mobileno','gender')