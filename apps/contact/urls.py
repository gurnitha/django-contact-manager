# apps/contact/urls.py

# Django modules
from django.urls import path

# Django loclas
from apps.contact import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detail/<int:id>/', views.detail, name="detail")
]
