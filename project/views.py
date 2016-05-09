from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Posts


def home(request):
	posts_list=Posts.objects.all()
	return render(request,'home.html', {'posts_list':posts_list})
