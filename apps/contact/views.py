# apps/contact/urls.py

# Django modules
from django.shortcuts import render

# Django locals
from apps.contact.models import Contact

# Create your views here.

def home(request):
	context = {
		'contacts':Contact.objects.all()
	}
	return render(request, 'index.html', context)