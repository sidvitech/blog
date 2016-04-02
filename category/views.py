from django.shortcuts import render, render_to_response
from .forms import UserCategoryForm, UserDeleteCategory
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from category.models import Category

def category(request):
	if request.method == "POST":
		form = UserCategoryForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = UserCategoryForm()

	return render(request, "category/category_form.html", { 'form': form })

def category_delete(request):
	name = request.POST.get('name')
	if request.method == "POST":
		form = UserDeleteCategory(request.POST)
		if form.is_valid():
			try:
				n = Category.objects.get(name=name)
				n.delete()
				print "hi"
			except Category.DoesNotExist:
				return HttpResponse("Category name not match. Plz check category name ")
			# except Category.MultipleObjectsReturned:
			# 	return HttpResponse("Category does not exist")

	else:
		form = UserDeleteCategory()

	return render(request, "category/delete.html", { 'form': form })
