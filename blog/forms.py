from django import forms
from . models import Blog

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


class PostForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'author', 'id': 'username', 'placeholder': 'Your name here'}))
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'name': 'title', 'placeholder': 'Insert your headline here'}))
    category = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control', 'name': 'category', 'id': 'category'}), choices=category_list)
    image = forms.ImageField()
    content = forms.Textarea(
        attrs={'class': 'form-control', 'name': 'content', 'placeholder': 'Write blog  content here'})

    class Meta:
        model = Blog
        fields = ['author', 'title', 'category', 'image', 'content']
