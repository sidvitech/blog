from django.shortcuts import render, render_to_response
from .forms import UserRegistrationForm, UserLoginForm,  UserPasswordResetForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, views
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_registration(request):
	# view_count = UserRegistration.objects.filter(view=True).count()
	
	if request.method == "POST":
		username = request.POST['reg_username']
		password = request.POST['reg_password']
		cpassword = request.POST['reg_confirm_password']
		email = request.POST['reg_email']
		if password == cpassword:
			try:
				user = User(username=username)
				user.set_password(password)
				user.email = email
				user.save()
				return HttpResponseRedirect('/post/mycomment/')
			except:
				messages.error(request, "your account all ready have create account")
		else:
			messages.error(request, "Password does not match........")
			return HttpResponseRedirect('') 
	else:
		user_form = UserRegistrationForm()

	return render(request, "userauth/user_registration_form.html")

def user_login(request):			
	if not request.user.is_authenticated():

		if request.method == "POST":
			username = request.POST.get('username', None)
			password = request.POST.get('password', None)

			auth = authenticate(username=username, password=password)
			if auth is not None:
				if auth.is_active:
					login(request, auth)
					return HttpResponseRedirect('/post/mycomment/')
				else:
					messages.error(request, "your account is not active")
			else:
				messages.error(request, "username or password not match")

			# try:
			# 	username = user_form.cleaned_data["username"]
			# 	password = user_form.cleaned_data["password"]
			# 	user =  authenticate(username=username, password=password)
			# 	if user is not None:
			# 		if user.is_active:
			# 			login(request, user)
			# 			return HttpResponseRedirect("/")
			# 		else:
			# 				messages.error(request, "Your account is not active.")
			# 	else:
			# 			messages.error(request, "username or password were incorrect.")
			# except:
			# 	pass
		else:
				user_form = UserLoginForm()
	else:
		messages.error(request, "User All Ready Login...")
		return HttpResponseRedirect("/")
	return render(request, "userauth/user_login.html")

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect('/userauth/user_login')
	else:
		messages.error(request, "User All Ready Logout...")
		return HttpResponseRedirect("/post/mycomment")

def main_page(request):
	return render_to_response('userauth/main_page.html', {'user': request.user})

def home(request):
	return render(request, "userauth/home.html")

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
		user_form = UserPasswordResetForm()
	return render(request, "userauth/password_reset_confirm.html", {'form': user_form})

def image(request): 
	image = UserRegistration.objects.all().order_by("name")
	context={'image': image}
	return render_to_response('userauth/image.html',context, )


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