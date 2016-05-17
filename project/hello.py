from django.core.urlresolvers import reverse

from django.contrib.auth.views import password_reset, password_reset_confirm

from django.shortcuts import render

def reset(request):
    return password_reset(request, template_name='reset.html',
        email_template_name='reset_email.html',
        subject_template_name='reset_subject.txt',
        post_reset_redirect=reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('success'))

# This view renders a page with success message.
def success(request):
  return render(request, "success.html")