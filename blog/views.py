from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import UserProfile, Posts, Category, PostData, CommentData, ReplyData
from blog.forms import UserForm, PostsForm, CategoryForm, UserProfileForm, PostDataForm, CommentDataForm, ReplyDataForm
from django.contrib.auth.models import User
from blog.bing_search import run_query
from django.contrib import messages
from django.db.models.functions import Value
from django.core.urlresolvers import reverse


context_dict={}
top_viewed=Posts.objects.order_by(Value('views').desc())[:6]
context_dict['top_viewed']=top_viewed
categories=Category.objects.all()[:6]
context_dict['categories']=categories


@login_required(login_url='/login/')
def blog(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	higher=6
	lower=0
	posts_list=Posts.objects.all()[:6]
	context_dict['posts_list']=posts_list
	context_dict['user']=user
	context_dict['profile']=profile
	categories=Category.objects.all()[:6]
	cat=Category.objects.all()
	for category in cat:
		count=Posts.objects.filter(category=category).count()
		category.total_posts=count
		category.save()
	context_dict['categories']=categories
	next=2
	previous=0
	for post in posts_list:
		try:
			count=CommentData.objects.filter(post_title=post).count()
			post.total_comments=count
			post.save()
		except:
			pass
	context_dict['next']=next 
	context_dict['previous']=previous
	return render(request,'blog/posts.html', context_dict)


@login_required(login_url='/login/')
def posts_list(request, page_no):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	higher=int(page_no)*6
	lower=int(higher)-6
	posts_list=Posts.objects.all()[lower:higher]
	count=Posts.objects.all().count()
	context_dict['posts_list']=posts_list
	context_dict['user']=user
	context_dict['profile']=profile
	next=int(page_no)+1
	previous=int(page_no)-1
	if higher<count:
		context_dict['next']=next 
	else:
		context_dict['next']=0
	if lower>0:
		context_dict['previous']=previous
	else:
		context_dict['previous']=0
	context_dict['page_no']=page_no
	return render(request,'blog/posts.html', context_dict)

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
def my_profile(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	context_dict['user']=user
	context_dict['profile']=profile
	posts_list=Posts.objects.filter(user=user)
	context_dict['posts_list']=posts_list
	return render(request,'blog/my_profile.html',context_dict)

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
	post=Posts.objects.get(id=post_id)
	auther=False
	if post.user==user:
		auther=True
	context_dict['auther']=auther
	cat=post.category
	see_also=Posts.objects.all().filter(category=cat)
	post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
	if post_data.view==0:
		post.views=post.views+1
		post_data.view+=1
		post_data.save()
		post.save()
	if request.method=="POST":
		comment=request.POST.get("comment")
		if comment:
			comments=CommentData()
			comments.user=user
			comments.post_title=post
			comments.userprofile=profile
			comments.comment=comment
			comments.save()
			return HttpResponseRedirect(".")
		else:
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
	try:
		view_comments=CommentData.objects.filter(post_title=post)
		context_dict['view_comments']=view_comments
		replies=ReplyData.objects.filter(post_title=post)
		context_dict['replies']=replies
	except:
		pass
	context_dict['post']=post
	context_dict['see_also']=see_also
	context_dict['user']=user
	context_dict['profile']=profile
	context_dict['post_data']=post_data
	return render(request,'blog/view_post.html', context_dict)

@login_required(login_url="/login/")
def add_reply(request, post_id, comment_id):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()

	if request.method=="POST":
		comment=CommentData.objects.get(id=comment_id)
		post=Posts.objects.get(id=post_id)
		reply=request.POST.get("reply")
		if reply:
			add_reply=ReplyData()
			add_reply.user=user
			add_reply.post_title=post
			add_reply.userprofile=profile
			add_reply.comment=comment
			add_reply.reply=reply
			add_reply.save()
			return HttpResponseRedirect(reverse('blog:view_post', kwargs={'post_id':post.id}))
		


@login_required(login_url='/login/')
def my_posts(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	higher=6
	lower=0
	posts_list=Posts.objects.filter(user=user)[:6]
	count=Posts.objects.filter(user=user).count()
	next=0
	if count>6:
		next=2
	previous=0
	categories=Category.objects.all()[:6]
	cat=Category.objects.all()
	for category in cat:
		count=Posts.objects.filter(category=category).count()
		category.total_posts=count
		category.save()
	context_dict['categories']=categories
	context_dict['posts_list']=posts_list
	context_dict['user']=user
	context_dict['profile']=profile
	context_dict['next']=next 
	context_dict['previous']=previous
	context_dict['page_no']=0
	return render(request,'blog/my_posts.html', context_dict)

@login_required(login_url='/login/')
def my_posts_list(request, page_no):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	higher=int(page_no)*6
	lower=int(higher)-6
	posts_list=Posts.objects.filter(user=user)[lower:higher]
	count=Posts.objects.all().count()
	context_dict['posts_list']=posts_list
	context_dict['user']=user
	context_dict['profile']=profile
	next=int(page_no)+1
	previous=int(page_no)-1
	if posts_list:
		if higher<count:
			context_dict['next']=next 
		else:
			context_dict['next']=0
		if lower>0:
			context_dict['previous']=previous
		else:
			context_dict['previous']=0
		context_dict['page_no']=page_no
	else:
		context_dict['next']=0
		context_dict['next']=0
		context_dict['previous']=0
		context_dict['page_no']=0
	return render(request,'blog/my_posts.html', context_dict)



@login_required(redirect_field_name='/login')
def search(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	context_dict['user']=user
	context_dict['profile']=profile
	if request.method=='POST' :
		context_dict['view']=1
		result_list=[]
		query=request.POST['query'].strip()
		posts=Posts.objects.filter(title__contains=query)
		user_profile=User.objects.filter(username__contains=query)
		context_dict['query']=query 
		context_dict['posts']=posts
		context_dict['user_profile']=user_profile
		if query:
			result_list=run_query(query)
		context_dict['result_list']=result_list
		return render(request,'blog/search.html',context_dict)
	return render(request,'blog/search.html',{'user':user, 'profile': profile})

	
@login_required(login_url='/login/')
def category_list(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
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
	category=Category.objects.get(name=category_name)
	context_dict['category_name']=category.name
	posts=Posts.objects.filter(category=category)
	context_dict['posts']=posts
	context_dict['category']=category
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
	context_dict['user']=user
	context_dict['profile']=profile
	if request.method=="POST":
		title=request.POST.get('title')
		details=request.POST.get('details')
		category_name=request.POST.get('category_name')
		category=Category.objects.get(name=category_name)
		if details:
			post.category=category
			post.title=title
			post.details=details
			try:
				thumb=request.FILES['thumb']
				post.thumb=thumb
			except:
				pass			
			post.save()
			return HttpResponseRedirect('/blog/')
		else:
			messages.error(request, "Details field is empty. ")
			context_dict['title']=title
			context_dict['post']=post
			context_dict['user']=user
			context_dict['profile']=profile
			return render(request,'blog/add_post.html', context_dict)
	context_dict['post']=post
	return render(request,'blog/add_post.html', context_dict)



@login_required(redirect_field_name='/login')
def add_category(request):
	username=request.user.username
	user=User.objects.get(username=username)
	category=Category(user_id=user.id)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	context_dict['user']=user
	context_dict['profile']=profile
	if request.method=="POST":
		name=request.POST.get('name')
		try:
			category=Category()
			category.name=name
			category.user=user
			category.total_posts=0
			category.save()
			return HttpResponseRedirect('/blog/')
		except:
			messages.error(request, "Category Already Exists!!") 
			context_dict['name']=name
			return render(request,'blog/add_category.html', context_dict)
	return render(request,'blog/add_category.html',context_dict)


@login_required(login_url='/login/')
def user_profile(request,u_id):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	user_user=User.objects.get(id=u_id)
	user_profile=UserProfile.objects.get(user_id=u_id)
	context_dict['user']=user
	context_dict['profile']=profile
	context_dict['user_profile']=user_profile
	context_dict['user_user']=user_user
	posts_list=Posts.objects.filter(user_id=u_id)
	context_dict['posts_list']=posts_list
	return render(request,'blog/user_profile.html',context_dict)


@login_required(login_url='/login/')
def delete_comment(request, post_id, comment_id):
	username=request.user.username
	user=User.objects.get(username=username)
	context_dict['user']=user
	post=Posts.objects.get(id=post_id)
	delete_comment=CommentData.objects.get(id=comment_id)
	delete_comment.delete()
	return HttpResponseRedirect(reverse('blog:view_post', kwargs={'post_id':post.id}))
	

@login_required(login_url='/login/')
def delete_post(request, post_id):
	username=request.user.username
	user=User.objects.get(username=username)
	context_dict['user']=user
	post=Posts.objects.get(id=post_id)
	cat_id=post.category_id
	post.delete()
	count=Posts.objects.filter(id=cat_id).count()
	category=Category.objects.get(id=cat_id)
	category.total_posts=count
	category.save()
	return HttpResponseRedirect("/blog/my_posts/?post_deleted")


@login_required(login_url='/login/')
def delete_reply(request, post_id, reply_id):
	username=request.user.username
	user=User.objects.get(username=username)
	context_dict['user']=user
	post=Posts.objects.get(id=post_id)
	delete_reply=ReplyData.objects.get(id=reply_id)
	delete_reply.delete()
	return HttpResponseRedirect(reverse('blog:view_post', kwargs={'post_id':post.id}))
	

