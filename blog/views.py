from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import UserProfile, Posts, Category
from blog.forms import UserForm, PostsForm, CategoryForm
from django.contrib.auth.models import User
from blog.bing_search import run_query
from django.contrib import messages

@login_required(login_url='/login/')
def home(request):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	
	categories=Category.objects.all()
	posts_list=Posts.objects.all()
	return render(request,'blog/posts.html', {'categories':categories, 'posts_list':posts_list, 'user':user, 'profile':profile})


def register(request):
	if request.method=='POST' :
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		username=request.POST.get('username')
		password1=request.POST.get('password1')
		password2=request.POST.get('password2')
		if password1:
			password=password1
			try:
				user=User(username=username)
				user.set_password(password)
				try:
					email = user.cleaned_email[email]
					user.email=email
				except:
					messages.error(request, "Email already used!")
					return HttpResponseRedirect('.')
				user.first_name=firstname
				user.last_name=lastname
				user.save()
				return HttpResponseRedirect('/login')
			except:
				messages.error(request, "Username already used!")
				return HttpResponseRedirect('.') 	
		else:
			messages.error(request, "Passwords does not match!!")
			return HttpResponseRedirect('.') 
		
	return render(request,'blog/register.html')
			

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username, password=password)
		if user:
			if user.is_active:
				request.session['user_id'] = user.id
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

@login_required(login_url='/login/')
def view_profile(request):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	return render(request,'blog/view_profile.html', {'user':user, 'profile':profile})

@login_required(login_url='/login/')
def edit_profile(request):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	if request.method=='POST' :
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		designation=request.POST.get('designation')
		lives_in=request.POST.get('lives_in')
		try:
			profile_picture=request.FILES['profile_picture']
		except:
			profile_picture=False
			pass
		if profile_picture:
			profile.profile_picture=profile_picture
			profile.save()
			messages.success(request,"Profile Picture Updated")
			return HttpResponseRedirect('.')
		else:	
			try:
				user.first_name=firstname
				user.last_name=lastname
				profile.designation=designation
				profile.lives_in=lives_in
				user.save()
				profile.save()
				success_message = "Profile Updated"
				messages.success(request, 'Profile details updated.')
				return HttpResponseRedirect('.')
			except:
				messages.error(request, "Username already used!")
				return HttpResponseRedirect('.')

	return render(request,'blog/edit_profile.html', {'user':user, 'profile':profile})

@login_required(redirect_field_name='/login')
def user_logout(request):
	del request.user
	logout(request)
	return HttpResponseRedirect('/')

@login_required(redirect_field_name='/login')
def view_post(request, post_id):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
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
	context_dict['user']=user
	context_dict['profile']=profile
	return render(request,'blog/view_post.html', context_dict)

@login_required(redirect_field_name='/login')
def search(request):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	result_list=[]
	if request.method=='POST' :
		query=request.POST['query'].strip()
		if query:
			result_list=run_query(query)
	return render(request,'blog/search.html',{'result_list': result_list, 'user':user, 'profile': profile})

@login_required(login_url='/login/')
def category_list(request):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	context_dict={}
	categories=Category.objects.all()
	context_dict['categories']=categories
	context_dict['user']=user
	context_dict['profile']=profile
	return render(request, 'blog/category_list.html', context_dict)

@login_required(login_url='/login/')
def category(request,category_name):
	username=request.user.username
	user=User.objects.get(username=username)
	profile=UserProfile.objects.get(user_id=user.id)
	context_dict={}
	category=Category.objects.get(name=category_name)
	context_dict['category_name']=category.name
	posts=Posts.objects.filter(category=category)
	context_dict['posts']=posts
	context_dict['category']=category
	categories=Category.objects.all()
	context_dict['categories']=categories
	context_dict['user']=user
	context_dict['profile']=profile
	return render(request, 'blog/category.html', context_dict)


