from django.shortcuts import render
from post.models import Post, MyComment
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm, MyCommentForm
# Create your views here.



def frontpage(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = PostForm()

	return render(request, "post/frontpage.html", { 'form': form })

def frontview(request):
	post = Post.objects.all()
	post_body_list =  [post.body for post in post]
	return render(request, "post/frontview.html", {'post_list': post_body_list})

def mycomment(request):
	if request.method == "POST":
		user_form = MyCommentForm(request.POST)
		if user_form.is_valid():
			user_form.save()

	else:
		user_form = MyCommentForm()

	return render(request, "post/comment.html", {'user_form': user_form})

def commentview(request):
	post = MyComment.objects.all()
	post_list =  [post for post in post]
	return render(request, "post/frontview.html", {'post_list': post_list})