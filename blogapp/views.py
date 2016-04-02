from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import BlogForm, DeleteBlogForm
from blogapp.models import Blogapp
# Create your views here.
def blog_view(request):
	return HttpResponse("blog app")
def blog_create(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = BlogForm()
	return render(request, 'blogapp/create_blog.html', {'form': form })
	# return HttpResponse("blog app")

def bolg_delete(request):
	# return HttpResponse("blog delete app")
	blogs = Blogapp.objects.all()
	blogname = request.POST.get('blogname')
	if request.method == "POST":
		form = DeleteBlogForm(request.POST)
		if form.is_valid():
			try:
				name = Blogapp.objects.get(blogname=blogname)
			except:
				return HttpResponse ('blogname not found...')	

			name.delete()
			messages.add_message(request, messages.INFO, 'Blog Deleted!')
	else:
		form =DeleteBlogForm()	
	return render(request, 'blogapp/dalete_blog.html', {'form': form ,'blogs':blogs })
	# blogname = request.POST.get('blogname')
	# if request.method == 'GET':
	# 	form = DeleteBlogForm(None)
	# else:
	# 	b1 = Blogapp.objects.get(blogname=blogname)
	# 	b1.delete()
	# return render(request, 'blogapp/dalete_blog.html', {'form': form ,'blogs':blogs })	


