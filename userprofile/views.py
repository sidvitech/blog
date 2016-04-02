from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from userprofile.models import userprof, profilepic, UserProfile
from userprofile.forms import userprofForm, profilepicForm, UserForm, UserForm1, UpdatepicForm
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def userprof_view(request):
	return HttpResponse("testing blog")


def adduserprof_view(request):	
	id = request.GET.get('id', None)
	if id is not None:
		userid = get_object_or_404(UserProfile,id=id)
	
	else:
		userid = None	
	
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		users_form = UserForm1(data = request.POST, instance = userid)
		if user_form.is_valid() and users_form.is_valid() :
			user = user_form.save()
			user.save()
			profile = users_form.save(commit = False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
					
			messages.add_message(request, messages.INFO, 'user added details!')
			# return HttpResponse("user submit details successfully")
			# return redirect('userprofile/userdetails.html', )
		else:
			print user_form.errors,users_form.errors
				
	else:
		user_form= UserForm()
		users_form=UserForm1(instance = userid)

	return render(request,'userprofile/userdetails.html',{'user_form':user_form, 'users_form':users_form,'userid':userid,},)	

def updateprofile_view(request):
	id = request.GET.get('id', None)
	if id is not None:
		userid = get_object_or_404(userprof,id=id)
	else:
		userid = None

	if request.method == 'POST':
		form = userprofForm(request.POST, instance=userid)
		profile_form = profilepicForm(data=request.POST,instance=userid)
		if form.is_valid() and profile_form.is_valid():
			form.save()
			profile = profile_form.save(commit=False)

			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']

				profile.save()	
			else:
				print profile_form.errors

			messages.add_message(request,messages.INFO,'user added details!')
			# return HttpResponse("user submit details successfully")
	else:
		form= userprofForm(instance=userid)
		profile_form = profilepicForm(instance=userid)

	return render(request,'userprofile/updateprofile.html',{'form':form,'userid':userid, 'profile_form':profile_form})	

def register(request):
	if request.method == 'POST':
		profile_form = profilepicForm(data=request.POST)
		if profile_form.is_valid():
			profile = profile_form.save(commit=False)
			
			if 'picture' in request.FILES:
				profile.picture=request.FILES['picture']

				profile.save()	
			else:
				print profile_form.errors

	else:
		profile_form = profilepicForm()

	return render(request,'userprofile/register.html', {'profile_form':profile_form})	

def edit_profile(request):
	user = request.user
	profile = user.userprofile
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		profile_form = UserForm1(request.POST, instance = profile)
		if all([user_form.is_valid(), profile_form.is_valid()]):
			user_form.save()
			profile_form.save()
			# return redirect('.')
	else:
		user_form = UserForm(instance = user)
		profile_form = UserForm1(instance = profile)

	return render (request,'userprofile/editprofile.html', {'user_form':user_form, 'profile_form':profile_form})			

def update_pic(request):
	user = request.user
	profile = user.userprofile
	print '1'
	if request.method == "POST":
		user_form = UpdatepicForm(data = request.POST,instance = profile)
		print '2'
		if user_form.is_valid():
			username = user_form.cleaned_data['username']
			picture = user_form.cleaned_data['picture']
			print '3'
			try:
				u = User.objects.get(username=username)
			except:
				return HttpResponse('username not found....')

			print '4'	
			p = user_form.save(commit = False)
			print '5'
			if 'picture' in request.FILES:
			 	p.picture=request.FILES['picture']

				p.save()	
				print '6'
			else:
				print user_form.errors
				print '7'	
	else:
		user_form=UpdatepicForm(instance = profile)			
	return render(request,'userprofile/update_pic.html',{'user_form':user_form})			
