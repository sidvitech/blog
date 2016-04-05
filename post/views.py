from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostAddForm, CommentAddForm, CommentEditForm
from post.models import PostAdd, CommentAdd
from userprofile.models import UserProfile

# Create your views here.
def post_view(request):
	posts = PostAdd.objects.all()
	post_body_list = [post.text for post in posts]
	# return HttpResponse("post app")
	return render(request, 'post/viewpost.html', {'posts':posts, 'post_list':post_body_list})

def post_create(request):
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
	return render(request, 'post/addpost.html', {'form': form})	

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

def comment_view(request):
	comments = CommentAdd.objects.all()
	return render(request, 'post/viewcomment.html',{'comments':comments})	

def comment_edit(request):
	queryset = CommentAdd.objects.all()
	if request.method == "POST":
		user_form = CommentEditForm(data = request.POST)
		if user_form.is_valid():
			comment = user_form.cleaned_data['comment']
			CommentAdd.objects.filter(id=2).update(
				comment=comment,
			)
			return HttpResponseRedirect('/post/commentview/')
		else:
			print form.errors
		
	else:
		user_form=CommentEditForm()			
	return render(request,'post/editcomment.html',{'user_form':user_form})	
	# return HttpResponse("post app")		

