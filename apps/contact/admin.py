# apps/contact/admin.py

# Django modules
from django.contrib import admin
from django.contrib.auth.models import Group

# Django locals
from apps.contact.models import Contact


# Customizing list disply in admin panel
class ContactAdmin(admin.ModelAdmin):
	list_display  = ('name', 'gender', 'email', 'info', 'phone')
	list_editable = ('info',)
	list_per_page = 6
	search_fields = ('name', 'gender', 'email', 'info', 'phone')
	list_filter   = ('gender', 'date_added')


# Register your models here.
admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)