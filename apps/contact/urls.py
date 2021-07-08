# apps/contact/urls.py

# Django modules
from django.urls import path

# Django loclas
from apps.contact import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.HomePageView.as_view(), name="home"),
    # path('detail/<int:id>/', views.detail, name="detail")
    path('detail/<int:pk>/', views.ContactDetailView.as_view(), name="detail")
]
