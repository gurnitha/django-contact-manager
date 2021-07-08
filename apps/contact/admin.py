# apps/contact/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.models import Group

# Django locals
from apps.contact.models import Contact

# Register your models here.
admin.site.register(Contact)
admin.site.unregister(Group)