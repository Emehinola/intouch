from django.shortcuts import render, redirect
from .models import Blog
from events.models import Event
from events.forms import *
from . forms import PostForm

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


def details(request, title):
    formatted_title = str(title.replace('%20', ' '))
    single_blog = Blog.objects.get(title=formatted_title, approved=True)
    events = Event.objects.all()

    context = {
        'details': single_blog,
        'events': events,
        'formatted_title': formatted_title
    }

    return render(request, 'blog/details.html', context)


def blog(request):
    posts = Blog.objects.filter(approved=True)
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)


def blog_category(request, category):
    posts = Blog.objects.filter(category=category, approved=True)
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


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('create_post/')
        else:
            pass
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/create_post.html', context)
