# apps/contact/urls.py

# Django modules
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'index.html')