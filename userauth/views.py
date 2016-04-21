from django.shortcuts import render, render_to_response
from .forms import UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, views
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

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
				HttpResponse("user form is not valid")
		else:
				user_form = UserLoginForm()
	else:
			return HttpResponseRedirect("/")
	return render(request, "userauth/user_login.html", {'form': user_form})

@login_required(login_url='/userauth/user_login/')
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/userauth/user_login')

@login_required(login_url='/userauth/user_login/')
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
			HttpResponse("user form is not valid")
	else:
		user_form = UserPasswordResetForm()
	return render(request, "userauth/password_reset_confirm.html", {'form': user_form})
