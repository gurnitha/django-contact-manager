# apps/contact/urls.py

# Django modules
from django.shortcuts import render, get_object_or_404

# Django locals
from apps.contact.models import Contact

# Create your views here.

def home(request):
	context = {
		'contacts':Contact.objects.all()
	}
	return render(request, 'index.html', context)


def detail(request, id):
	context = {
		'contacts':get_object_or_404(Contact, pk=id)
	}
	return render(request, 'detail.html', context)