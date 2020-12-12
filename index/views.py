from django.shortcuts import render, redirect
from blog.models import Blog
from events.models import Event, Vacancy, FormControl, GiveAway
from events.forms import *
from .models import HomeViewCount

# Create your views here.


def home(request):
    technologies_post = Blog.objects.filter(category='Technology')
    forms = None
    message = None
    viewsCount, create = HomeViewCount.objects.get_or_create(id=1)
    viewsCount.views += 1  # increasing the views count per visit
    viewsCount.save()
    try:
        giveAway = GiveAway.objects.get(active=True)
    except:
        giveAway = None
        message = 'Nothing to display yet. Thanks'
    all_forms = [
        [WhoProposedForm(request.POST), WhoProposedForm(), ],
        [MostConsumedFoodForm(request.POST), MostConsumedFoodForm(), ],
        [WhenDisvirginForm(request.POST), WhenDisvirginForm()],
        [WhatGivesYouJoyInIphoneForm(
            request.POST), WhatGivesYouJoyInIphoneForm()],
        [CauseOfBreakUp(request.POST), CauseOfBreakUp()],
        [HowManyTimesDoYouBrushForm(request.POST),
         HowManyTimesDoYouBrushForm()],
        [HowMuchDoYouSpendOnCardForm(
            request.POST), HowMuchDoYouSpendOnCardForm()],
        [BathSurveyForm(request.POST), BathSurveyForm()],
        [ResponsiblePersonForm(request.POST),
         ResponsiblePersonForm()],
        [CraziestStuffForm(request.POST), CraziestStuffForm()]
    ]

    formControl = FormControl.objects.all()
    for field in formControl:
        question = field.question
    posts = Blog.objects.filter(approved=True)[:5]
    events = Event.objects.all()
    vacancies = Vacancy.objects.all()

    if request.method == 'POST':
        for form in all_forms:
            if form[0].question == question:
                forms = form[0]
        if forms.is_valid():
            forms.save()
            # forms = MostConsumedFoodForm()
            return redirect('home')

    else:
        for form in all_forms:
            if form[1].question == question:
                forms = form[1]

    context = {
        'posts': posts,
        'events': events,
        'vacancies': vacancies,
        'forms': forms,
        'current': question,
        'giveaway': giveAway,
        'message': message,
        'technologies': technologies_post
    }
    return render(request, 'index/home.html', context)


def contact(request):
    return render(request, 'index/contact.html')


def about(request):
    return render(request, 'index/about.html')
