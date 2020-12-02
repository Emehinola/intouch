from django.contrib import admin
from .models import Event, Vacancy, GiveAway, BathSurvey, CauseOfBreakUp, CraziestStuff, HowManyTimesDoYouBrush, HowMuchDoYouSpendOnCard, KindOfPeopleYouLike, MostConsumedFood, ResponsiblePerson,  WhatGivesYouJoyInIphone, WhenDisvirgin, FormControl, WhoProposed

# Register your models here.
admin.site.register(Event)
admin.site.register(Vacancy)
admin.site.register(WhoProposed)
admin.site.register(BathSurvey)
admin.site.register(CauseOfBreakUp)
admin.site.register(CraziestStuff)
admin.site.register(HowManyTimesDoYouBrush)
admin.site.register(HowMuchDoYouSpendOnCard)
admin.site.register(KindOfPeopleYouLike)
admin.site.register(MostConsumedFood)
admin.site.register(ResponsiblePerson)
admin.site.register(WhatGivesYouJoyInIphone)
admin.site.register(WhenDisvirgin)
admin.site.register(FormControl)
admin.site.register(GiveAway)
