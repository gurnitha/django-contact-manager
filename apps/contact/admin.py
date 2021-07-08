# apps/contact/admin.py

# Django modules
from django.contrib import admin

# Django locals
from apps.contact.models import Contact

# Register your models here.
admin.site.register(Contact)