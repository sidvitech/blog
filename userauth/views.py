from django.shortcuts import render, render_to_response
from .forms import UserRegistrationForm, UserLoginForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
	return render(request, "userauth/login.html", {'form': user_form})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def main_page(request):
	return render_to_response('userauth/main_page.html', {'user': request.user})