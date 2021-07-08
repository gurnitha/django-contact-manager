# apps/contact/urls.py

# Django modules
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

# Django locals
from apps.contact.models import Contact

# Create your views here.

# # Homepage 1
# def home(request):
# 	context = {
# 		'contacts':Contact.objects.all()
# 	}
# 	return render(request, 'index.html', context)


# Homepage 2
class HomePageView(ListView):
	template_name = 'index.html'
	model = Contact 
	context_object_name = 'contacts'	


# # Detailpage 1
# def detail(request, id):
# 	context = {
# 		'contact':get_object_or_404(Contact, pk=id)
# 	}
# 	return render(request, 'detail.html', context)


# Detailpage 2
class ContactDetailView(DetailView):
	template_name = 'detail.html'
	model = Contact
	context_object_name = 'contact'	
