from django.urls import path
from . import views

urlpatterns = [
    path(r'contact/', views.contact, name="contact"),
    path(r'about/', views.about, name="about"),
    path(r'', views.home, name="home")
]
