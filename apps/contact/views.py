# apps/contact/urls.py

# Django modules
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView

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


# # Searchpage 1
# def search(request):
# 	context = {
# 		'search_term':search_term
# 	}
# 	return render(request, 'search.html', context)


# # Searchpage 2
# def search(request):
# 	if request.GET:
# 		search_term = request.GET['search_term']
# 		context = {
# 			'search_term':search_term
# 		}
# 		return render(request, 'search.html', context)
# 	else:
# 		return redirect('home')	


# # Searchpage 3
# def search(request):
# 	if request.GET:
# 		search_term = request.GET['search_term']
# 		search_result = Contact.objects.filter(name__icontains=search_term)
# 		context = {
# 			'search_term':search_term,
# 			'contacts':search_result
# 		}
# 		return render(request, 'search.html', context)
# 	else:
# 		return redirect('home')	


# Searchpage 4
def search(request):
	if request.GET:
		search_term = request.GET['search_term']
		search_result = Contact.objects.filter(
			Q(name__icontains=search_term) |
			Q(email__icontains=search_term) |
			Q(info__icontains=search_term) |
			Q(phone__iexact=search_term)
		)
		context = {
			'search_term':search_term,
			'contacts':search_result
		}
		return render(request, 'search.html', context)
	else:
		return redirect('home')	


# -------------- CRUD VIEWS ----------------

# CRUD: CreateView 
class ContactCreateView(CreateView):
	model = Contact
	template_name = 'crud/create.html'
	fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
	success_url = '/'


# # CRUD: UpdateView 1
# class ContactUpdateView(UpdateView):
# 	model = Contact
# 	template_name = 'crud/update.html'
# 	fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
# 	success_url = '/'


# CRUD: UpdateView 2
class ContactUpdateView(UpdateView):
	model = Contact
	template_name = 'crud/update.html'
	fields = ['name', 'email', 'phone', 'info', 'gender', 'image']

	# After fullfiling and submitting the form
	# redirect it to its own detail page
	def form_valid(self, form):
		instance = form.save()
		return redirect('detail', instance.pk)
