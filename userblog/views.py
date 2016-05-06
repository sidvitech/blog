from django.shortcuts import render, render_to_response
from .forms import BlogForm, UserDeleteBlog
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from userblog.models import Blog


def blog(request):
	view_count = Blog.objects.filter(view=True).count()

	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/userblog/blog/')

	else:
		form = BlogForm()
	return render(request, "blog/blog_form.html", { 'form': form, 'view_count': view_count })

def blog_delete(request):
	blog_name = request.POST.get('blog_name')
	if request.method == "POST":
		form = UserDeleteBlog(request.POST)
		if form.is_valid():
			try:
				n = Blog.objects.get(blog_name=blog_name)
				n.delete()
				return HttpResponseRedirect('/userblog/blog_delete/')
				print "hi"
			except Blog.DoesNotExist:
				return HttpResponse("Category name not match. Plz check category name ")
			# except Category.MultipleObjectsReturned:
			# 	return HttpResponse("Category does not exist")

	else:
		form = UserDeleteBlog()

	return render(request, "blog/delete.html", { 'form': form })
