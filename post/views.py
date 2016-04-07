from django.shortcuts import render
from post.models import Post, MyComment, Like
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm, MyCommentForm, UserDeleteComment
# Create your views here.



def frontpage(request):
	if request.method == "POST":
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			print request.FILES
			form.save()

	else:
		form = PostForm()

	post = Post.objects.all()
	post_list =  [post for post in post]
	return render(request, "post/frontpage.html", { 'form': form, 'post_list': post_list })

def frontview(request):
	post = Post.objects.all()
	post_body_list =  [post.body for post in post]
	return render(request, "post/frontview.html", {'post_list': post_body_list})

def mycomment(request):
	if request.method == "POST":
		user_form = MyCommentForm(request.POST)
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/post/mycomment/')

	else:
		user_form = MyCommentForm()

	return render(request, "post/comment.html", {'user_form': user_form})

def commentview(request):
	data = False
	like_count = Like.objects.filter(like=True).count()
	if request.user.is_authenticated():
		try:
			obj = Like.objects.get(user=request.user)
			data = obj.like
		except:
			pass

	if request.method == "POST":
		unlike = request.POST.get('unlike')
		like = request.POST.get('like')
		if request.user.is_authenticated():
			if like:
				user, condition = Like.objects.get_or_create(user=request.user)
				user.like = True
				user.save()
				return HttpResponseRedirect('/post/commentview/')
			if unlike:
				like_obj = Like.objects.get(user=request.user)
				like_obj.like = False
				like_obj.save()
				return HttpResponseRedirect('/post/commentview/')
		else:
			return HttpResponseRedirect('/userauth/user_login/')

	post = MyComment.objects.all()
	post_list =  [post for post in post]

	return render(request, "post/postlist.html", {'post_list': post_list, 'data': data, 'like_count':like_count })

def comment_delete(request):
	if request.user.is_authenticated():
		title = request.POST.get('title')
		if request.method == "POST":
			form = UserDeleteComment(request.POST)
			if form.is_valid():
				try:
					n = MyComment.objects.get(title=title)
					n.delete()
					return HttpResponseRedirect('/post/comment_delete/')
				except MyComment.DoesNotExist:
					return HttpResponse("Category name not match. Plz check category name ")
				# except Category.MultipleObjectsReturned:
				# 	return HttpResponse("Category does not exist")

		else:
			form = UserDeleteComment()

		post = MyComment.objects.all()
		comment_list =  [post for post in post]
	return render(request, "post/comment_delete.html", { 'form': form, 'comment_list': comment_list })
