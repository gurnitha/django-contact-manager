# apps/contact/urls.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home(request):
	context = {
		'status': 'Passing data to template',
		'age': 12
	}
	return render(request, 'index.html', context)