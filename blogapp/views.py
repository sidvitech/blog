from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import BlogForm, DeleteBlogForm
from blogapp.models import Blogapp
from post.models import PostAdd, CommentAdd
# Create your views here.
def blog_view(request):
	blog_list = Blogapp.objects.all()
	post_list = PostAdd.objects.all()
	return render(request,'blogapp/blog_view.html',{'blog_list':blog_list,'post_list':post_list})
	
def blog_create(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			blogapp = form.save(commit = False)
			blogapp.user = request.user
			blogapp.save()
			
	else:
		form = BlogForm()
	return render(request, 'blogapp/create_blog.html', {'form': form })
	# return HttpResponse("blog app")

def bolg_delete(request):
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
	

