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
    ('result', 'Survey result'),
    ('enterpreneur', 'Enterpreneur'),
    ('job', 'Job')
]


class Blog(models.Model):
    # author = models.ForeignKey(
    #     User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog images',
                              height_field=None)
    category = models.CharField(max_length=50, choices=category_list)
    approved = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Blog posts'

    def __str__(self):
        return f'{self.title} | {self.time}'
