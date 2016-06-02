from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from post.models import Post, MyComment, Like
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .forms import PostForm
from django.template.loader import get_template
from django.core.mail import EmailMessage, send_mail
from django.template import RequestContext, Context
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from django.contrib import messages
from category.models import Category
from userprofile.models import UserProfile
from django.core import serializers
# Create your views here.

def post_detail(request, pk):
    context = {}
    post_list = get_object_or_404(Post, pk=pk)
    post_comment = MyComment.objects.all()
    print post_comment
    print "Hi comment"
    data = False
    like_count = Like.objects.filter(like=True, post=post_list).count()

    username=request.user.username
    user=User.objects.get(username=username)
    try:
        profile=UserProfile.objects.get(user_id=user.id)
    except:
        profile=UserProfile()

# comment Like
    if request.method == "POST":
        unlike = request.POST.get('unlike')
        like = request.POST.get('like')
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_authenticated():
            if like:
                user, condition = Like.objects.get_or_create(post=post, user=request.user)
                user.like = True
                user.save()
                return HttpResponseRedirect(reverse('post:post_detail', kwargs={'pk':pk}))
            if unlike:
                like_obj = Like.objects.get(post=post, user=request.user)
                like_obj.like = False
                like_obj.save()
                return HttpResponseRedirect(reverse('post:post_detail', kwargs={'pk':pk}))
        else:
            messages.error(request, "User not login........")
            return HttpResponseRedirect('/userauth/user_login/')
# Post comment
        comment=request.POST.get("comment")
        if comment:
            comments = MyComment.objects.create(post=post, user=request.user)
            comments.title=comment
            comments.save()
            return HttpResponseRedirect(reverse('post:post_detail', kwargs={'pk':pk}))
        else:
            pass

    context["data"] = data
    context["like_count"] = like_count
    context["post_comment"] = post_comment
    context["post_list"] = post_list 
    context["profile"] = profile 

    return render(request, "post/post_detail.html", context)


@login_required(login_url='/userauth/user_login/')
def create_post(request):
    username=request.user.username
    user=User.objects.get(username=username)
    post=Post(user_id=user.id)
    try:
        profile=UserProfile.objects.get(user_id=user.id)
    except:
        profile=UserProfile()

    context_dict={}
    context_dict['user']=user
    context_dict['profile']=profile
    if request.method=="POST":
        title=request.POST.get('title')
        details=request.POST.get('details')
        category_name=request.POST.get('category_name')
        try:
            thumb=request.FILES['thumb']
            post.image=thumb
        except:
            thumb=False
            pass

        try:
            category=Category.objects.get(name=category_name)
            post.category=category
        except:
            messages.error(request, "Oops! Something went wrong") 
            context_dict['title']=title
            context_dict['details']=details
            context_dict['category_name']=category_name
            context_dict['thumb']=thumb
            return HttpResponseRedirect('/post/post_list/', context_dict)
        post.title=title
        post.body=details
        post.save()
        return HttpResponseRedirect('/post/post_list/')
    else:
        category_list=Category.objects.all()
    context_dict['post']=post
    context_dict['categories']=category_list

    return render(request, "post/create_post.html", {'post': post, 'categories': category_list})

def post_list(request):
    data = False
    like_count = Like.objects.filter(like=True).count()
    data=False
    comment_count = MyComment.objects.filter(comment=True).count()
    if request.user.is_authenticated():
        try:
          obj = MyComment.objects.get(user=request.user)
          data = obj.comment
        except:
          pass

    if request.user.is_authenticated():
        username = request.user.username
        user_post = Post.objects.all().filter(user__username=username)
    else:
        user_post = Post.objects.all()

    return render(request, "post/post_list.html", { 'user_post': user_post, 'data': data, 'like_count': like_count, 'comment_count': comment_count})

def all_post(request, page_no):
    user_post = Post.objects.all()
    data = False
    like_count = Like.objects.filter(like=True).count()
    higher=int(page_no)*6
    lower=int(higher)-6
    posts_list=Post.objects.all()[lower:higher]
    count=Post.objects.all().count()
    if request.user.is_authenticated():
        try:
          obj = Like.objects.get(user=request.user)
          data = obj.like
        except:
          pass

    data=False
    comment_count = MyComment.objects.filter(comment=True).count()
    if request.user.is_authenticated():
        try:
          obj = MyComment.objects.get(user=request.user)
          data = obj.comment
        except:
          pass
    next=int(page_no)+1
    previous=int(page_no)-1
    if higher<count:
        context_dict['next']=next 
    else:
        context_dict['next']=0
    if lower>0:
        context_dict['previous']=previous
    else:
        context_dict['previous']=0
    context_dict['page_no']=page_no
    return render(request, "post/postlist.html",context_dict, {'user_post': user_post, 'like_count': like_count, 'comment_count': comment_count})

def gallery_image(request):
    post_image = Post.objects.all()

    return render(request, 'post/images.html', {'post_image': post_image})
def delete_comment(request, pk):
    try:
        comment = MyComment.objects.get(post__user=request.user, pk=pk)
        post_id = comment.post.id
        comment.delete()
        return HttpResponseRedirect(reverse('post:post_detail', kwargs={'pk':post_id}))
    except:
        return HttpResponse("user does not match. or comment does not exist.")

def category_android(request):
    if request.user.is_authenticated():
        try:
            category_list = Category.objects.all()
            cat_post = Post.objects.all().filter(category=category_list)
        except:
            pass
    else:
        return HttpResponse("Posts does not exist")

    return render(request, 'post/blog_post.html', {'cat_post': cat_post})

def category_education(request):
    if request.user.is_authenticated():
        try:
            category_list = Category.objects.all().filter(name='Education')
            cat_post = Post.objects.all().filter(category=category_list)
        except:
            pass
    else:
        return HttpResponse("Posts does not exist")

    return render(request, 'post/category_post.html', {'cat_post': cat_post})