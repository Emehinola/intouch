from django.urls import path
from . import views
from blog import views as blog_views

urlpatterns = [
    path(r'contact/', views.contact, name="contact"),
    path(r'about/', views.about, name="about"),
    path(r'create_post/', blog_views.create_post, name="create_post"),
    path(r'', views.home, name="home")
]
