from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from post.models import Post, MyComment, Like, Contact
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm, MyCommentForm, UserDeleteComment, ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
# Create your views here.


def post_list(request, pk):
	context = {}
	post_list = get_object_or_404(Post, pk=pk)
	post_comment = Post.objects.all()

		# # comment Like
		# if request.method == "POST":
		# 	user_form = MyCommentForm(request.POST)
		# 	if user_form.is_valid():
		# 		try:
		# 			post = Post.objects.get(title)
		# 			data = user_form.save(commit=False)
		# 			data.user = request.user
		# 			data.post_name = 
		# 			data.save()
		# 			return HttpResponseRedirect('')
		# else:
		# 	user_form = MyCommentForm()

	post = MyComment.objects.all()
	comment_display =  [post for post in post]

	# context["user_form"] = user_form

	context["post_comment"] = post_comment
	context["post_list"] = post_list  
	return render(request, "post/post_list.html", context)


@login_required(login_url='/userauth/user_login/')
def frontpage(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			print request.FILES
			obj = form.save()
			return HttpResponseRedirect(reverse('post:post_list', kwargs={'pk':obj.pk}))
	else:
		form = PostForm()

	
	return render(request, "post/frontpage.html", { 'form': form})

def frontview(request):
	post = Post.objects.all()
	post_body_list =  [post.body for post in post]
	return render(request, "post/frontview.html", {'post_list': post_body_list})


def mycomment(request):
	if request.user.is_authenticated():
		username = request.user.username
		print username

		user_post = Post.objects.all().filter(user__username=username)
		# print user_post
	else:
		user_post = Post.objects.all()
		print user_post

	return render(request, "post/comment.html", { 'user_post': user_post})

def commentview(request):
	data = False
	# like_count = Like.objects.filter(like=True).count()
	# if request.user.is_authenticated():
	# 	try:
	# 		obj = Like.objects.get(user=request.user)
	# 		data = obj.like
	# 	except:
	# 		pass

	# if request.method == "POST":
	# 	unlike = request.POST.get('unlike')
	# 	like = request.POST.get('like')
	# 	if request.user.is_authenticated():
	# 		if like:
	# 			user, condition = Like.objects.get_or_create(user=request.user)
	# 			user.like = True
	# 			user.save()
	# 			return HttpResponseRedirect('/post/commentview/')
	# 		if unlike:
	# 			like_obj = Like.objects.get(user=request.user)
	# 			like_obj.like = False
	# 			like_obj.save()
	# 			return HttpResponseRedirect('/post/commentview/')
	# 	else:
	# 		return HttpResponseRedirect('/userauth/user_login/')



	return render(request, "post/postlist.html", {'data': data, 'like_count':like_count })

def comment_delete(request):
	if request.user.is_authenticated():
		title = request.POST.get('title')
		if request.method == "POST":
			form = UserDeleteComment(request.POST)
			if form.is_valid():
				try:
					n = MyComment.objects.get(user=request.user, title=title)
					n.delete()
					return HttpResponseRedirect('/post/mycomment/')
				except MyComment.DoesNotExist:
					return HttpResponse("Category name not match. or user does not match. Plz check category name ")
				# except Category.MultipleObjectsReturned:
				# 	return HttpResponse("Category does not exist")

		else:
			form = UserDeleteComment()

		post = MyComment.objects.all()
		comment_list =  [post for post in post]
	return render(request, "post/comment_delete.html", { 'form': form, 'comment_list': comment_list })


def delete_comment(request, pk):
	try:
		comment = MyComment.objects.get(user=request.user, pk=pk)
		comment.delete()
		return HttpResponseRedirect('/post/post_list/')
	except:
		return HttpResponse("user does not match. or comment does not exist.")


def contact(request):  
	user = User.objects.get(id=2)
	user_email = user.email
	if request.user.is_authenticated():
		user_name = request.POST.get('user_name')
		print user_name
		if request.method == 'POST':
			form_class = ContactForm(request.POST)
			if form_class.is_valid():
				contact_name = request.POST.get('contact_name', '')
				contact_email = request.POST.get('contact_email', '')
				form_content = request.POST.get('content', '')
				# Email the profile with the 
				# contact information
				template = get_template('contact_template.txt')
				context = Context({'contact_name': contact_name,
					'contact_email': contact_email,
					'form_content': form_content,
				})
				print "Hi...."
				print contact_name
				print contact_email
				print form_content
				content = template.render(context)
				send_mail(contact_name, form_content, user_email,
				[contact_email], fail_silently=False)
				return redirect('/post/contact/')
		else:
			form_class=ContactForm()
			# pass
	else:
		return HttpResponseRedirect('/userauth/user_login/')
	return render(request, 'post/contact.html', {'form_class': form_class})
