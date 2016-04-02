from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostAddForm, CommentAddForm
from post.models import PostAdd, CommentAdd

# Create your views here.
def post_view(request):
	return HttpResponse("post app")

def post_create(request):
	posts = PostAdd.objects.all()
	post_body_list = [post.text for post in posts]
	if request.method == "POST":
		form = PostAddForm(request.POST)
		if form.is_valid():
			profile = form.save(commit = False)
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
		else:
			print form.errors

	else:
		form = PostAddForm()
	return render(request, 'post/addpost.html', {'form': form, 'posts':posts, 'post_list':post_body_list})	

def comment_create(request):
	if request.method == "POST":
		form = 	CommentAddForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			print form.errors
	else:
		form = CommentAddForm()
	return render(request, 'post/addcomment.html', {'form': form })				