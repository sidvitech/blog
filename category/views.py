from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .forms import UserCategoryForm, UserDeleteCategory
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from category.models import Category
from userprofile.models import UserProfile
from post.models import Post

def create_category(request):
    ca_list = Category.objects.all()
    if request.method == "POST":
        form = UserCategoryForm(request.POST)
        if form.is_valid():
            us = form.save(commit=False)
            us.user = request.user
            us.save()
            return HttpResponseRedirect('/category/create_category/')   
    else:
        form = UserCategoryForm()

    return render(request, "category/create_category_form.html", { 'form': form , 'ca_list': ca_list })

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


def category_detail(request, pk):
    context = {}
    ca_list = Category.objects.all()
    detail_cat = get_object_or_404(Category, pk=pk)
    username=request.user.username
    user=User.objects.get(username=username)
    try:
            profile=UserProfile.objects.get(user=user)

    except:

            profile=UserProfile()

    user_post = Post.objects.all().filter(category=detail_cat)
    context["user_post"] = user_post
    context["ca_list"] = ca_list
    context["detail_cat"] = detail_cat 
    context["profile"] = profile 
    return render(request, "category/detail_cat.html", context)