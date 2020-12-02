from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category_list = [
    ('General', 'General'),
    ('Education', 'Education'),
    ('Business', 'Business'),
    ('Entertainment', 'Entertainment'),
    ('Sports', 'Sports'),
    ('Technology', 'Technology'),
    ('Religion', 'Religion'),
    ('Gossips', 'Gossips'),
    ('Health', 'Health'),
    ('Food', 'Food and Nutrients'),
    ('Fitness', 'Fitness'),
    ('Career', 'Career'),
    ('result', 'Survey result')
]


class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog images',
                              height_field=None, width_field=None, max_length=None)
    category = models.CharField(max_length=50, choices=category_list)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        return f'{self.title} | {self.time}'
