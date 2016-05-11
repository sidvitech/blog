from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from blog.models import UserProfile, Posts, Category
from blog.forms import UserForm, PostsForm, UserProfileForm, CategoryForm
from django.contrib.auth.models import User
from blog.bing_search import run_query


def home(request):
	categories=Category.objects.all()
	posts_list=Posts.objects.all()
	return render(request,'blog/posts.html', {'categories':categories, 'posts_list':posts_list})


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
	return HttpResponseRedirect('/')


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
	context_dict={}
	categories=Category.objects.all()
	post=Posts.objects.get(id=post_id)
	post.views=post.views+1
	post.save()
	context_dict['post']=post
	context_dict['categories']=categories
	return render(request,'blog/view_post.html', context_dict)


def search(request):
	result_list=[]
	if request.method=='POST' :
		query=request.POST['query'].strip()
		if query:
			result_list=run_query(query)
	return render(request,'blog/search.html',{'result_list': result_list})


def category_list(request):
	context_dict={}
	categories=Category.objects.all()
	context_dict['categories']=categories
	return render(request, 'blog/category_list.html', context_dict)


def category(request,category_name):
	context_dict={}
	category=Category.objects.get(name=category_name)
	context_dict['category_name']=category.name
	posts=Posts.objects.filter(category=category)
	context_dict['posts']=posts
	context_dict['category']=category
	categories=Category.objects.all()
	context_dict['categories']=categories
	return render(request, 'blog/category.html', context_dict)


