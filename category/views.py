from django.shortcuts import render, render_to_response
from .forms import UserCategoryForm
from django.http import HttpResponse

# Create your views here.
def category(request):
	if request.method == "POST":
		form = UserCategoryForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = UserCategoryForm()

	return render(request, 'category/category_form.html', { 'form': form })
	# return HttpResponse("testing category")