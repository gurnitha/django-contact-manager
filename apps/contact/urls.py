# apps/contact/urls.py

# Django modules
from django.urls import path

# Django loclas
from apps.contact import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.HomePageView.as_view(), name="home"),
    # path('detail/<int:id>/', views.detail, name="detail")
    path('detail/<int:pk>/', views.ContactDetailView.as_view(), name="detail"),
    path('searc/', views.search, name="search"),
    path('contact/create', views.ContactCreateView.as_view(), name="create"),
    path('contact/update/<int:pk>', views.ContactUpdateView.as_view(), name="update"),
    path('contact/delete/<int:pk>', views.ContactDeleteView.as_view(), name="delete"),
    path('signup/', views.SignUpView.as_view(), name="signup"),
]
