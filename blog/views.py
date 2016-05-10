from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from blog.models import UserProfile, Posts
from blog.forms import UserForm, PostsForm, UserProfileForm
from django.contrib.auth.models import User
from blog.bing_search import run_query


def home(request):
	posts_list=Posts.objects.all()
	return render(request,'blog/posts.html', {'posts_list':posts_list})


def register(request):
	registered=False
	if request.method=='POST':
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile=profile_form.save(commit=False)
			profile.user=user.id
			profile.save()
			registered=True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form=UserForm()
		profile_form=UserProfileForm()
	return render(request,'blog/register.html',{'user_form':user_form,'profile_form':profile_form,  'registered':registered})

			

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/?login_successful')
			else:
				error_msg="Your Account Is Disabled."
				return render(request, 'blog/login.html', {'error_msg':error_msg})
		else:
			error_msg="Invalid login details supplied."
			return render(request,'blog/login.html',{'error_msg':error_msg})
	else:
		return render(request, 'blog/login.html', {})

def view_profile(request):
	user=UserProfile.objects.get(username=username)
	return render(request,'blog/edit_profile.html', {'user':user})

def edit_profile(request):
	user=UserProfile.objects.get(username=username)
	return render(request,'blog/edit_profile.html', {'user':user})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/blog/login/')


def add_post( request):
	if request.method=='POST':
		form=PostsForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.save()
		else:
			print form.errors
	else:
		form=PostsForm()
	context_dict={'form':form}
	return render(request, 'blog/add_post.html', context_dict)

def view_post(request, post_id):
	post=Posts.objects.get(id=post_id)
	return render(request,'blog/view_post.html', {'post':post})


def search(request):
	result_list=[]
	if request.method=='POST' :
		query=request.POST['query'].strip()
		if query:
			result_list=run_query(query)
	return render(request,'blog/search.html',{'result_list': result_list})

