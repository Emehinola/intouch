from django import forms
from .models import WhoProposed, MostConsumedFood, WhenDisvirgin, WhatGivesYouJoyInIphone, HowManyTimesDoYouBrush, HowMuchDoYouSpendOnCard, ResponsiblePerson, KindOfPeopleYouLike, CauseOfBreakUp, CraziestStuff, BathSurvey

choices = [
    ('nobody', 'Nobody'),
    ('male', 'I, the boy'),
    ('female', 'I, the girl'),
    ('male', 'The boy'),
    ('female', 'The girl'),

]


class CraziestStuffForm(forms.ModelForm):
    question = "What is the most craziest thing you have ever done for the sake of love?"
    description = "You would get amazed when you hear the actions some people have taken for those they love. This survey helps to get different people's view on this"
    answer = forms.TextInput(
        attrs={'class': 'textbox', 'placeholder': 'Your response here'})

    class Meta:
        model = CraziestStuff
        fields = ['answer']


class WhoProposedForm(forms.ModelForm):
    question = "Before getting into your current relationship, Who made the proposal to the other person?"
    description = "In some relationships, the proposal is first made by the female patner. This survey helps to keep track of the ratio of female proposals to that of the male"
    answer = forms.ChoiceField(choices=choices)

    class Meta:
        model = WhoProposed
        fields = ['answer']


class MostConsumedFoodForm(forms.ModelForm):
    question = "What kind of food did you eat today?"
    description = "This survey helps to collect data based on the kind of food that is mostly consumed in Nigeria.  "
    answer = forms.CharField(label=question, widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'foodConsumed', 'placeholder': 'Your response please'}))

    class Meta:
        model = MostConsumedFood
        fields = ['answer']


sex_age = [
    ('below 10 years', 'Below 10 years old'),
    ('between 10 - 15', 'Between 10 - 15'),
    ('between 15 - 20', 'Between 15 - 20'),
    ('above 20 years', 'Above 20 years of age'),
    ('still a virgin', 'Still a virgin')
]


class WhenDisvirginForm(forms.ModelForm):
    question = "If you are not a virgin, when did you get disvirgin?"
    description = "The purpose of this survey is to know the age range within which most girls are disvirgin"
    answer = forms.ChoiceField(
        choices=sex_age, widget=forms.Select(attrs={'class': 'select-wrap form-control'}))

    class Meta:
        model = WhenDisvirgin
        fields = ['answer']


class WhatGivesYouJoyInIphoneForm(forms.ModelForm):
    question = "What made you like Iphone or Apple product?"
    description = "Different people buy or use apple products for some funny reasons. This survey helps to get different reasons people prefer iphones"
    answer = forms.CharField(widget=forms.TextInput(
        attrs={'class': '', 'name': ''}))

    class Meta:
        model = WhatGivesYouJoyInIphone
        fields = ['answer']


class CauseOfBreakUp(forms.ModelForm):
    question = "If you had ever been into any relationship, What is the Cause of your Break Up?"
    description = "This survey helps to get the highest cause of relationships break up"
    answer = forms.CharField(widget=forms.TextInput(
        attrs={'class': '', 'name': ''}))

    class Meta:
        model = CauseOfBreakUp
        fields = ['answer']


class HowManyTimesDoYouBrushForm(forms.ModelForm):
    question = "How many times do you brush daily?"
    description = "This survey helps to get the break down of the number of times different people brush in a day"
    answer = forms.IntegerField(required=True)

    class Meta:
        model = HowManyTimesDoYouBrush
        fields = ['answer']


select = [
    ('100 to 200', '#100 to #200'),
    ('200 to 500', '#200 to #500'),
    ('500 to 700', '#500 to #700'),
    ('700 to 1000', '#700 to #1000'),
    ('1000 to 1500', '#1000 to #1500'),
    ('1500 to 2000', '#1500 to #2000'),
    ('2000 to 2500', '#2000 to #2500'),
    ('2500 to 3000', '#2500 to #3000'),
    ('3000 to 4000', '#3000 to #4000'),
    ('4000 to 5000', '#4000 to #5000'),
    ('5000 and above', '#5000 and above')
]


class HowMuchDoYouSpendOnCardForm(forms.ModelForm):
    question = "How much do you spend on airtime weekly?"
    description = "This survey helps to keep track of the  approximated amount spent on recharge card by Nigerians on a weekly basis"
    answer = forms.RadioSelect(choices=select)

    class Meta:
        model = HowMuchDoYouSpendOnCard
        fields = ['answer']


bath_choices = [
    ('once', 'Once'),
    ('two', 'Two times'),
    ('three', 'Three times'),
    ('four', 'Four times'),
    ('varies', 'It varies'),

]


class BathSurveyForm(forms.ModelForm):
    question = "How many times do you bath a day?"
    description = "This survey helps to keep track of the average number of times people take their bath daily"
    answer = forms.ChoiceField(
        choices=bath_choices, widget=forms.Select(attrs={'class': 'select-wrap form-control'}))

    class Meta:
        model = BathSurvey
        fields = ['answer']


class ResponsiblePersonForm(forms.ModelForm):
    question = "How do you describe someone who is responsible?"
    description = "Different people describe a RESPONSIBLE person in different ways. This survey helps to get the view of people on this"
    answer = forms.Textarea(attrs={'class': 'form-control', 'name': ''})

    class Meta:
        model = ResponsiblePerson
        fields = ['answer']
