from django.shortcuts import render
from .models import Blog
from events.models import Event
from events.forms import *

# Create your views here.

all_surveys = [
    WhoProposedForm(),
    MostConsumedFoodForm(),
    WhenDisvirginForm(),
    WhatGivesYouJoyInIphoneForm(),
    CauseOfBreakUp(),
    HowManyTimesDoYouBrushForm(),
    HowMuchDoYouSpendOnCardForm(),
    BathSurveyForm(),
    ResponsiblePersonForm(),
    CraziestStuffForm()
]


def details(request, id):
    single_blog = Blog.objects.get(id=id)
    events = Event.objects.all()

    context = {
        'details': single_blog,
        'events': events

    }

    return render(request, 'blog/details.html', context)


def blog(request):
    posts = Blog.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_category(request, category):
    posts = Blog.objects.filter(category=category)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog/category.html', context)


def survey_topics(request):
    topics = []
    for topic in all_surveys:
        topics.append(topic.question)

    return render(request, 'blog/survey_topics.html', {'topics': topics})
