# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Django loclas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.contact.urls')),
    path('', include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# Customizing admin texts
admin.site.site_header = "Admin Panel Contact Manager"
admin.site.index_title = "Welcome to Contact Manager"
admin.site.site_title  = "Control Panel"