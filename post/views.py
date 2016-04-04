from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostAddForm, CommentAddForm
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
	b = PostAdd.objects.all()
	comments = CommentAdd.objects.all()
	
	if comments != None:
		if b != None:
			for comm in comments:
				var = comm.postname
				print var
				for b1 in b:
					var1 = b1.postname
					print var1
					# print b1.postname
					if var is var1:
						print 45


	comments = CommentAdd.objects.all()
	return render(request, 'post/viewcomment.html',{'b':b,'comments':comments})	

def comment_edit(request):
	user = request.user
	print user
	profile = user.userprofile
	print profile
	# print '1'
	# if request.method == "POST":
	# 	user_form = UpdatepicForm(data = request.POST,instance = profile)
	# 	print '2'
	# 	if user_form.is_valid():
	# 		username = user_form.cleaned_data['username']
	# 		picture = user_form.cleaned_data['picture']
	# 		print '3'
	# 		try:
	# 			u = User.objects.get(username=username)
	# 		except:
	# 			return HttpResponse('username not found....')

	# 		print '4'	
	# 		p = user_form.save(commit = False)
	# 		print '5'
	# 		if 'picture' in request.FILES:
	# 		 	p.picture=request.FILES['picture']

	# 			p.save()	
	# 			print '6'
	# 		else:
	# 			print user_form.errors
	# 			print '7'	
	# else:
	# 	user_form=UpdatepicForm(instance = profile)			
	# return render(request,'userprofile/update_pic.html',{'user_form':user_form})	
	return HttpResponse("post app")		

