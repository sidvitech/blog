from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Posts
from django.contrib.auth.models import User
from blog.models import UserProfile

@login_required(login_url='/login/')
def home(request):
	username=request.user.username
	user=User.objects.get(username=username)
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()

	posts_list=Posts.objects.all()
	return render(request,'home.html', {'posts_list':posts_list, 'user':user, 'profile':profile})



