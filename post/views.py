from django.shortcuts import render, get_object_or_404
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
	comments = CommentAdd.objects.all()
	# postname='skn'
	# count = CommentAdd.objects.filter(_CommentAdd__postname=postname).count()
	# print count
	if request.user.is_authenticated():
		if request.method == "POST":
			print 1
			form = 	CommentAddForm(request.POST)
			print 2
			if form.is_valid():
				print 3
				postname = request.POST.get('postname')
				post = PostAdd.objects.get(postname=postname)
				print post
				comment = form.save(commit = False)
				comment.user = request.user
				comment.postname = post
				comment.save()
				print form.cleaned_data['comment']
				
				return HttpResponseRedirect('/post/')
				print 4
			else:
				print form.errors
				print 4
		else:
			form = CommentAddForm()
			print 5
	else:
		return HttpResponse("You are not authorised person.")
	

	
	return render(request, 'post/viewpost.html', {'form': form, 'posts':posts, 'post_list':post_body_list, 'comments':comments})

def post_create(request):
	if request.method == "POST":
		form = PostAddForm(request.POST, request.FILES)
		if form.is_valid():
			profile = form.save(commit = False)
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			if 'video' in request.FILES:
				profile.video = request.FILES['video']	
			profile.save()
			form = PostAddForm()
		else:
			print form.errors

	else:
		form = PostAddForm()
	return render(request, 'post/addpost.html', {'form': form})	



def comment_edit(request):
	queryset = CommentAdd.objects.all()
	title = request.POST.get('comment')
	print title
	if request.user.is_authenticated():	
		if request.method == "POST":
			user_form = CommentEditForm(data = request.POST)
			if user_form.is_valid():
				postname = user_form.cleaned_data['postname']
				print postname
				comment1 = user_form.cleaned_data['comment']
				c = CommentAdd.objects.filter(postname=postname)
				print c
				CommentAdd.objects.filter(postname=postname).update(
					comment=comment1,
				)
				return HttpResponseRedirect('/post/commentview/')
			else:
				print user_form.errors
		else:
			user_form=CommentEditForm()			
	else:
		return HttpResponse("You are not authorised person.")			
		
			
	return render(request,'post/editcomment.html',{'user_form':user_form})	
		
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

def comment_ed(request):
	user = request.user
	profile = user.userprofile
	if request.method == "POST":
		user_form = CommentEditForm(data = request.POST,instance = profile)
		if user_form.is_valid():
			# postname = user_form.cleaned_data['postname']
			# comment = user_form.cleaned_data['comment']
			# try:

				u = CommentAdd.objects.get(user=request.user)
				u=user_form.save(commit = False)
				u.save()
			# except:
			# 	return HttpResponse('postname not found')
				print u
	else:
		user_form = CommentEditForm(instance = profile)
	return render(request,'post/editcomment.html',{'user_form':user_form})		
