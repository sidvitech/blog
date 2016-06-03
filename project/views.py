from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Posts
from django.contrib.auth.models import User
from blog.models import UserProfile
from django.contrib import messages

@login_required(login_url='/login/')
def home(request):
	username=request.user.username
	user=User.objects.get(username=username)
	total=User.objects.all().count()
	try:
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		profile=UserProfile()

	posts=Posts.objects.all().count()
	all_posts=Posts.objects.all()
	views=0
	for post in all_posts:
		views+=post.views
	return render(request,'home.html', {'posts':posts, 'user':user, 'profile':profile, 'total':total, 'views':views})

@login_required(login_url='/login/')
def lock(request):
	try:
		username=request.user.username
		user=User.objects.get(username=username)
		profile=UserProfile.objects.get(user_id=user.id)
	except:
		user=0
		profile=0
		pass	
	if request.method=='POST':
		del request.user
		logout(request)	
		if request.POST.get('username'):
			username=request.POST.get('username')
		else:
			username=username
		password=request.POST.get('password')
		new_user=authenticate(username=username, password=password)
		if new_user:
			del request.user
			logout(request)
			request.session['user_id'] = new_user.id
			login(request, new_user)
			return HttpResponseRedirect('/?login_successful')
		else:
			messages.error(request, "Invalid login details provided.")
			return HttpResponseRedirect('.')
	else:
		return render(request, 'lock.html', {'user':user, 'profile':profile})



def handler404(request):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},context_instance=RequestContext(request))
    response.status_code = 500
    return response

