from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
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
categories=Category.objects.all().order_by("-total_posts")[:5]
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
	cat=Category.objects.all()
	for category in cat:
		count=Posts.objects.filter(category=category).count()
		category.total_posts=count
		category.save()
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
		else:
			user.first_name=''
		if lastname:
			user.last_name=lastname
		else:
			user.last_name=''
		if profession:
			profile.profession=profession
		else:
			profile.profession=''
		if lives_in:
			profile.lives_in=lives_in
		else:
			profile.lives_in=''

		user.save()
		profile.save()

		return HttpResponseRedirect('/blog/my_profile')

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
	try:
		view_comments=CommentData.objects.filter(post_title=post).order_by("-created_on")
		context_dict['view_comments']=view_comments
		replies=ReplyData.objects.filter(post_title=post).order_by("-created_on")
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
def like_post(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	if request.method == "GET":
		post_id = request.GET.get('postid')
	likes = 0
	if post_id:
		post = Posts.objects.get(id=int(post_id))
		post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
		likes = post.likes
		if post and post_data.like < 1:
			post_data.like+=1
			likes = likes + 1
			post.likes =  likes
			post_data.save()
			post.save()
	return HttpResponse(likes)


@login_required(login_url="/login/")
def unlike_post(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	if request.method == "GET":
		post_id = request.GET.get('postid')
	likes = 0
	if post_id:
		post = Posts.objects.get(id=int(post_id))
		post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
		likes = post.likes
		if post and post_data.like > 0:
			post_data.like-=1
			likes = likes - 1
			post.likes =  likes
			post_data.save()
			post.save()
	return HttpResponse(likes)


@login_required(login_url="/login/")
def star_post(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	if request.method == "GET":
		post_id = request.GET.get('postid')
	stars = 0
	if post_id:
		post = Posts.objects.get(id=int(post_id))
		post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
		stars = post.stars
		if post and post_data.star < 1:
			post_data.star+=1
			stars = stars + 1
			post.stars =  stars
			post_data.save()
			post.save()
	return HttpResponse(stars)


@login_required(login_url="/login/")
def unstar_post(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	if request.method == "GET":
		post_id = request.GET.get('postid')
	stars = 0
	if post_id:
		post = Posts.objects.get(id=int(post_id))
		post_data, condition=PostData.objects.get_or_create(user=user, post_title=post)
		stars = post.stars
		if post and post_data.star > 0:
			post_data.star-=1
			stars = stars - 1
			post.stars =  stars
			post_data.save()
			post.save()
	return HttpResponse(stars)


@login_required(login_url="/login/")
def post_comment(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	comment_text=None
	if request.method == "GET":
		comment_text = request.GET.get('comment')
		post_id = request.GET.get('postid')
	if post_id:
		post = Posts.objects.get(id=int(post_id))
		newcomment=CommentData()
		newcomment.user=user
		newcomment.post_title=post
		newcomment.userprofile=profile
		newcomment.comment=comment_text
		newcomment.save()
		return JsonResponse({"comment":comment_text, "newid":newcomment.id})
	return HttpResponse(None)


@login_required(login_url="/login/")
def edit_comment(request):
	print 1
	comment_id=None
	new_comment=None
	if request.method=="GET":
		new_comment=request.GET.get("newcomment")
		comment_id=request.GET.get("commentid")
	print 2
	if comment_id and new_comment:
		print 3
		editcomment=CommentData.objects.get(id=comment_id)
		print 4
		editcomment.comment=new_comment
		print 5
		editcomment.save()
		print 6
		return JsonResponse({"comment":editcomment.comment, "newid":comment_id})
	print 7
	return HttpResponse(None)


@login_required(login_url="/login/")
def add_reply(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()
	post_id = None
	comment_id=None
	reply_text=None
	if request.method == "GET":
		reply_text = request.GET.get('reply')
		post_id = request.GET.get('postid')
		comment_id = request.GET.get('commentid')
	if post_id and comment_id:
		post = Posts.objects.get(id=int(post_id))
		comment=CommentData.objects.get(id=int(comment_id))
		newreply=ReplyData()
		newreply.user=user
		newreply.post_title=post
		newreply.userprofile=profile
		newreply.comment=comment
		newreply.reply=reply_text
		newreply.save()
		return JsonResponse({"reply":reply_text, "newid":newreply.id})
	return HttpResponse(None)


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
	categories=Category.objects.all().order_by("name")
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
			return HttpResponseRedirect('/blog/my_posts/')
		else:
			messages.error(request, "Details field is empty. ")
			context_dict['title']=title
			context_dict['post']=post
			context_dict['user']=user
			context_dict['profile']=profile
			context_dict['category_name']=category_name
			return render(request,'blog/add_post.html', context_dict)
	context_dict['post']=post
	return render(request,'blog/add_post.html', context_dict)


@login_required(redirect_field_name='/login')
def edit_post(request, post_id):
	username=request.user.username
	user=User.objects.get(username=username)
	post=Posts(id=post_id)
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
	else:
		context_dict['post']=post
	return render(request,'blog/edit_post.html', context_dict)


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


def delete_comment(request):
	comment_id=None
	if request.method == "GET":
		comment_id = request.GET.get('commentid')
	if comment_id:
		delete_comment=CommentData.objects.get(id=comment_id)
		delete_comment.delete()
		return HttpResponse(comment_id)
	return HttpResponse(None)


def delete_reply(request):
	reply_id=None
	if request.method=="GET":
		reply_id=request.GET.get('replyid')
	if reply_id:
		delete_reply=ReplyData.objects.get(id=reply_id)
		delete_reply.delete()
		return HttpResponse(reply_id)
	return HttpResponse(None)
	

