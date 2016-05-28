from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import UserProfile, Posts, Category, PostData
from blog.forms import UserForm, PostsForm, CategoryForm, UserProfileForm, PostDataForm
from django.contrib.auth.models import User
from blog.bing_search import run_query
from django.contrib import messages

@login_required(login_url='/login/')
def home(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	categories=Category.objects.all()
	posts_list=Posts.objects.all()
	return render(request,'blog/posts.html', {'categories':categories, 'posts_list':posts_list, 'user':user, 'profile':profile})

def register(request):
	username=request.user.username
	if username:
		return HttpResponseRedirect('/')
	else:
		if request.method=='POST' :
			firstname=request.POST.get('firstname')
			lastname=request.POST.get('lastname')
			email=request.POST.get('email')
			print 1
			birthdate=request.POST.get('birthdate')
			print 2
			username=request.POST.get('username')
			password1=request.POST.get('password1')
			password2=request.POST.get('password2')
			if password1==password2:
				password=password1
				try:
					user=User(username=username)
					user.set_password(password)
					try:
						count=User.objects.filter(email=email).count()
						if count==0:
							user.email=email
						else:
							raise forms.ValidationError(u'This email address is already registered.')
					except:
						messages.error(request,"Email already used!")
						return render(request,'blog/register.html', { 'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username, 'birthdate':birthdate })
					user.first_name=firstname
					user.last_name=lastname
					try:
						user.save()
						profile=UserProfile()
						profile.user_id=user.id
						profile.birthdate=birthdate
						profile.save()
						return HttpResponseRedirect('/login')
					except:
						messages.error(request, "Birthdate problem!")
						return render(request,'blog/register.html', { 'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username, 'birthdate':birthdate })	
				except:
					messages.error(request, "Username already used!")
					return render(request,'blog/register.html', { 'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username, 'birthdate':birthdate })
			else:
				messages.error(request, "Passwords does not match!!")
				return render(request,'blog/register.html', { 'firstname':firstname, 'lastname':lastname, 'email':email, 'username':username, 'birthdate':birthdate })

		return render(request,'blog/register.html')



def user_login(request):
	username=request.user.username
	if username:
		return HttpResponseRedirect('/blog')
	else:
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
					messages.error(request, "Your Account Is Disabled.")
					return HttpResponseRedirect('.')
			else:
				messages.error(request, "Invalid login details provided.")
				return HttpResponseRedirect('.')
		else:
			return render(request, 'blog/login.html')

@login_required(login_url='/login/')
def view_profile(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	return render(request,'blog/view_profile.html', {'user':user, 'profile':profile})

@login_required(login_url='/login/')
def edit_profile(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	if request.method=='POST' :
		profile.user_id=user.id
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		profession=request.POST.get('profession')
		lives_in=request.POST.get('lives_in')
		email=request.POST.get('email')
		birthdate=request.POST.get('birthdate')
		try:
			profile_picture=request.FILES['profile_picture']
		except:
			profile_picture=False
			pass

		if profile_picture:
			if profile.profile_picture is not "/user/no-image.jpg":
				profile.profile_picture.delete(True)
			profile.profile_picture=profile_picture
			
			profile.save()
			return HttpResponseRedirect('.')
			
		try:
			if email:
				count=User.objects.filter(email=email).count()
				print user.email
				print email
				if user.email==email:
					user.email=email
				elif count==0:
					user.email=email
				else:
					raise forms.ValidationError(u'This email address is already registered.')
		except:
			messages.error(request,"Email Id already registered!")
			return HttpResponseRedirect('.')
		if birthdate:
			profile.birthdate=birthdate
		if firstname:
			user.first_name=firstname
		if lastname:
			user.last_name=lastname
		if profession:
			profile.profession=profession
		if lives_in:
			profile.lives_in=lives_in

		user.save()
		profile.save()

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
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	context_dict={}
	categories=Category.objects.all()
	post=Posts.objects.get(id=post_id)
	cat=post.category_id
	see_also=Posts.objects.all().filter(category_id=cat)
	post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
	if post_data.view==0:
		post.views=post.views+1
		post_data.view+=1
		post_data.save()
	if request.method=="POST":
		if request.POST.get("like"):
			if post_data.like==0:
				post_data.like+=1
				post.likes+=1
				post_data.save()
				post.save()
		if request.POST.get("unlike"):
			if post_data.like==1:
				post_data.like-=1
				post.likes-=1
				post_data.save()
				post.save()
		if request.POST.get("star"):
			if post_data.star==0:
				post.stars+=1
				post_data.star+=1
				post_data.save()
				post.save()
		if request.POST.get("unstar"):
			if post_data.star==1:
				post_data.star-=1
				post.stars-=1
				post_data.save()
				post.save()
		return HttpResponseRedirect(".")			
	post.save()
	context_dict['post']=post
	context_dict['categories']=categories
	context_dict['see_also']=see_also
	context_dict['user']=user
	context_dict['profile']=profile
	context_dict['post_data']=post_data
	return render(request,'blog/view_post.html', context_dict)

@login_required(redirect_field_name='/login')
def search(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
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
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
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
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
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


@login_required(redirect_field_name='/login')
def add_post(request):
	username=request.user.username
	user=User.objects.get(username=username)
	post=Posts(user_id=user.id)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	context_dict={}
	context_dict['user']=user
	context_dict['profile']=profile
	if request.method=="POST":
		title=request.POST.get('title')
		details=request.POST.get('details')
		category_name=request.POST.get('category_name')
		try:
			thumb=request.FILES['thumb']
		except:
			thumb=False
			pass

		try:
			category=Category.objects.get(name=category_name)
			category.total_posts
			total_posts=category.total_posts
			category.total_posts=total_posts+1
			post.category_id=category.id
		except:
			messages.error(request, "Oops! Something went wrong")
			context_dict['title']=title
			context_dict['details']=details
			context_dict['category_name']=category_name
			context_dict['thumb']=thumb
			return render(request,'blog/add_post.html', context_dict)
		post.title=title
		post.details=details
		post.thumb=thumb
		post.save()
		category.save()
		return HttpResponseRedirect('/blog/')
	else:
		category_list=Category.objects.all()
	context_dict['post']=post
	context_dict['categories']=category_list
	return render(request,'blog/add_post.html', context_dict)





