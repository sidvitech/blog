from django.shortcuts import render, render_to_response
from .forms import UserRegistrationForm, UserLoginForm,  UserPasswordResetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, views
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.


def user_registration(request):
	if request.method == "POST":
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			user = user_form.save(commit=False)
			password = user_form.cleaned_data["password1"]
			user.set_password(password)
			user.save()

	else:
		user_form = UserRegistrationForm()

	return render(request, "userauth/user_registration_form.html", { 'form': user_form })

def user_login(request):
	if not request.user.is_authenticated():

		if request.method == "POST":
			user_form = UserLoginForm(request.POST)
			if user_form.is_valid():
				username = user_form.cleaned_data["username"]
				password = user_form.cleaned_data["password"]
				user =  authenticate(username=username, password=password)
				if user is not None:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect("/")
					else:
							messages.error(request, "Your account is not active.")
				else:
						messages.error(request, "username or password were incorrect.")
		else:
				user_form = UserLoginForm()
	else:
			return HttpResponseRedirect("/")
	return render(request, "userauth/user_login.html", {'form': user_form})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def main_page(request):
	return render_to_response('userauth/main_page.html', {'user': request.user})

def home(request):
	return render(request, "userauth/home.html")

def user_reset_password(request):
	if request.method == "POST":
		user_form = UserPasswordResetForm(request.POST)
		if user_form.is_valid():
			username = user_form.cleaned_data['username']
			password1 = user_form.cleaned_data['password1']
			password2 = user_form.cleaned_data['password2']
			try:
				u = User.objects.get(username=username)
			except:
				return HttpResponse('username not found....')

			data = u.check_password(user_form.cleaned_data['password1'])
			print data
			if data:
				u.set_password(password2)
				u.save()
				return HttpResponseRedirect('/userauth/user_login/')
			else:
				return HttpResponse("old password incorrect......")
	else:
		user_form = UserPasswordResetForm()
	return render(request, "userauth/password_reset_confirm.html", {'form': user_form})

# def password_change(request):
# 	if request.method == 'POST':
# 		form = PasswordChangeForm(user=request.user, data=request.POST)
# 	if form.is_valid():
# 		form.save()
# 		update_session_auth_hash(request, form.user)
# 	else:

# def change_password(request):
# 	template_response = views.password_change(request)
# 	return template_response