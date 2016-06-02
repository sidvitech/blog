from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from .forms import UserProfileForm, EditProfileForm
from django.contrib.auth.models import User
# from blog.bing_search import run_query
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
def update_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    try:
        profile = UserProfile.objects.get(user_id=user.id)
    except:
        profile = UserProfile()
    if request.method == 'POST' :
        profile.user_id = user.id
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        designation = request.POST.get('designation')
        lives_in = request.POST.get('lives_in')
        email = request.POST.get('email')
        birthdate = request.POST.get('birthdate')
        try:
            profile_picture = request.FILES['profile_picture']
        except:
            profile_picture = False
            pass

        if profile_picture:
            if profile.profile_picture is not "/user/no-image.jpg":
                profile.profile_picture.delete(True)
            profile.profile_picture = profile_picture
            
            profile.save()
            return HttpResponseRedirect('.')
            
        try:
            if email:
                count = User.objects.filter(email=email).count()
                print user.email
                print email
                if user.email == email:
                    user.email = email
                elif count == 0:
                    user.email = email
                else:
                    raise forms.ValidationError(u'This email address is already registered.')
        except:
            messages.error(request,"Email Id already registered!")
            return HttpResponseRedirect('.')
        if birthdate:
            profile.birthdate = birthdate
        if firstname:
            user.first_name = firstname
        if lastname:
            user.last_name = lastname
        if designation:
            profile.designation = designation
        if lives_in:
            profile.lives_in = lives_in

        user.save()
        profile.save()

        return HttpResponseRedirect('.')

    return render(request, "userprofile/update.html", {'user':user, 'profile':profile})

def user_profile(request):
    username = request.user.username
    user = User.objects.get(username=username)
    try:
        profile = UserProfile.objects.get(user_id=user.id)
    except:
        profile = UserProfile()
    return render(request, 'userprofile/profile.html', {'profile': profile})