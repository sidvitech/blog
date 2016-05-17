from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
	if request.method=='POST' :
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		email=request.POST.get('email')
		# profile_picture=request.POST.get['profile_picture']
		username=request.POST.get('username')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		if password1==password2:
			password=password1
			try:
				user=User(username=username)
				user.set_password(user.password)
				user.set_email(user.email)
				profile=UserProfile(user_id=user.id)
				profile.first_name=firstname
				profile.last_name=lastname
				profile.email=email
				# profile.profile_picture=profile_picture
				user.save()
				profile.save()
				registered=True
			except:
				registered=False
				pass
			else:
				registered=False
	if registered==True:
		HttpResponseRedirect('/login/?Registered')
	return render(request,'blog/register.html',{'registered':registered})
			

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


def view_post(request, post_id):
	context_dict={}
	categories=Category.objects.all()
	post=Posts.objects.get(id=post_id)
	cat=post.category_id
	see_also=Posts.objects.all().filter(category_id=cat)
	post.views=post.views+1
	post.save()
	context_dict['post']=post
	context_dict['categories']=categories
	context_dict['see_also']=see_also
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


