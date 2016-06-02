from django.shortcuts import render, render_to_response
from .forms import UserCategoryForm, UserDeleteCategory
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from category.models import Category

def create_category(request):
	if request.method == "POST":
		form = UserCategoryForm(request.POST)
		if form.is_valid():
			us = form.save(commit=False)
			us.user = request.user
			us.save()
			return HttpResponseRedirect('/category/create_category/')	
	else:
		form = UserCategoryForm()

	return render(request, "category/create_category_form.html", { 'form': form })

def category_list(request):
	ca_list = Category.objects.all()
	print ca_list
	print "hi....list"

	return render(request, "category/category_list.html", {'ca_list': ca_list})

def delete_category(request, pk):
	try:
		category = Category.objects.get(user=request.user, pk=pk)
		category.delete()
		return HttpResponseRedirect('/category/category_list/')
	except:
		return HttpResponse("user does not match. or comment does not exist.")

		