from django.shortcuts import render
from post.models import Post
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PostForm
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