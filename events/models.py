from django.db import models

# Create your models here.


class Event(models.Model):  # Events model here
    instructor = models.CharField(max_length=50)
    title = models.CharField(max_length=300)
    description = models.TextField()
    venue = models.CharField(max_length=100)
    paid_or_free = models.CharField(max_length=10)
    date_and_time = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time_created']
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.title

# VACANCY MODEL


class Vacancy(models.Model):
    position = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    whatsapp_contact = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    job_description = models.TextField()
    application_message = models.TextField()
    deadline = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.position

# survey models

# Bath survey


bath_choices = [
    ('once', 'Once'),
    ('two', 'Two times'),
    ('three', 'Three times'),
    ('four', 'Four times'),
    ('varies', 'It varies'),

]

# this model controls the form to display


class FormControl(models.Model):
    question = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Forms Control'

    def __str__(self):
        return self.question


class BathSurvey(models.Model):
    answer = models.CharField(max_length=20, choices=bath_choices)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Bath surveys'

    def __str__(self):
        return self.answer


# who proposed

class WhoProposed(models.Model):
    answer = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Who proposed surveys'

    def __str__(self):
        return self.answer

# craziest thing ever done for th sake of love


class CraziestStuff(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Craziest thing ever done for the sake of love surveys'

    def __str__(self):
        return self.answer

# most consumed food on sundays


class MostConsumedFood(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Most consumed food on sundays'

    def __str__(self):
        return self.answer


# when you were disvirgin


class WhenDisvirgin(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'When you were disvirgin'

    def __str__(self):
        return self.answer

# cause of your previous break up


class CauseOfBreakUp(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'What is the cause of your previous break up'

    def __str__(self):
        return self.answer

# What gives you joy in iphone


class WhatGivesYouJoyInIphone(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'What gives you joy in using iphone'

    def __str__(self):
        return self.answer

# Hown much you nspend on


class HowMuchDoYouSpendOnCard(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'How much do you spend on recharge card'

    def __str__(self):
        return self.answer

# How much you nspend on


class ResponsiblePerson(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'How to desribe a reponsible'

    def __str__(self):
        return self.answer


class KindOfPeopleYouLike(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Which kind of girl or boy do you like?'

    def __str__(self):
        return self.answer


class HowManyTimesDoYouBrush(models.Model):
    answer = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'How many times do you brush a day'

    def __str__(self):
        return self.answer


# GiveAway model


class GiveAway(models.Model):
    desc = models.TextField()
    offer = models.TextField()
    active = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'GiveAways'

    def __str__(self):
        return self.desc


class WhatsAppGiveAway(models.Model):  # cash giveAway
    winningCode = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'WhatsApp GiveAway'

    def __str__(self):
        return self.winningCode
