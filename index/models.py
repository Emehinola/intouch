from django.db import models

# Create your models here.

# home page view, i.e the surveys views


class HomeViewCount(models.Model):
    views = models.IntegerField(default=0)  # number of views or visits
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Views'

    def __str__(self):
        return f'{self.views}'
