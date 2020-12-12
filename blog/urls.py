from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'details/(?P<title>.+)$', views.details, name='details'),
    url(r'(?P<category>\w+)$', views.blog_category, name='category'),
    url(r'survey_topics/', views.survey_topics, name='survey_topics'),
    url(r'', views.blog, name='blog')
]
