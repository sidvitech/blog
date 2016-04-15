from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth.models import User
from userprofile.models import userprof, profilepic, UserProfile
from userprofile.forms import userprofForm, profilepicForm, UserForm, UserForm1, UpdatepicForm,updateprofileform,updateprofileform1
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

def userprof_view(request):
	username = request.user
	uname=request.user.get_username()
	fullname=request.user.get_full_name()
	fname=request.user.get_short_name()
	lname=request.user.last_name
	email=request.user.email
	mobileno=username.userprofile.mobileno
	gender=username.userprofile.gender
	pic = username.userprofile.picture
	u = User.objects.get(username=username)
	
	
	return render(request,'userprofile/view_profile.html',{'fullname':fullname,'uname':uname,'fname':fname,'lname':lname,'email':email,'gender':gender,'pic':pic,'mobileno':mobileno})
	# return HttpResponse("testing blog")


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
			profile = users_form.save()
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

def updateuserprof_view(request):
	user = request.user
	profile = user.userprofile
	if request.method == 'POST':
		user_form = updateprofileform(data=request.POST)
		users_form = updateprofileform1(data=request.POST)
		if user_form.is_valid() and users_form.is_valid() :
			username = user_form.cleaned_data['username']
			email = user_form.cleaned_data['email']
			first_name = user_form.cleaned_data['first_name'] 
			last_name = user_form.cleaned_data['last_name']
			mobileno=users_form.cleaned_data['mobileno']
			# mobileno = request.POST.get('mobileno')
			gender = request.POST.get('gender')

			User.objects.filter(username=username).update(
					email=email,
					first_name=first_name,
					last_name=last_name,
					
				)
			UserProfile.objects.filter(user__username=username).update(
					mobileno=mobileno,
					gender=gender,
				)	
			user_form= updateprofileform()
			users_form=updateprofileform1()			
		else:
			print user_form.errors,users_form.errors
	else:
		user_form= updateprofileform()
		users_form=updateprofileform1()		
	return render(request,'userprofile/updateprofile.html',{'user_form':user_form,'users_form':users_form})
					


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
	print user
	print profile
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
				print u
			except:
				return HttpResponse('username not found....')
			# UserProfile.objects.filter(user__username=username).update(
			# 		picture=picture,
			# 	)	
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
			user_form=UpdatepicForm()	
	else:
		user_form=UpdatepicForm(instance = profile)			
	return render(request,'userprofile/update_pic.html',{'user_form':user_form})	

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
