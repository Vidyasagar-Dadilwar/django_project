from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        "author": "Emily",
        "date_posted": 15,
        "title": "My First Post",
        "content": "This is my first blog post.",
    },
    {
        "author": "David",
        "date_posted": 20,
        "title": "Hello World",
        "content": "Just saying hello to the world.",
    },
    {
        "author": "Sarah",
        "date_posted": 25,
        "title": "My Favorite Book",
        "content": "I just finished reading my favorite book.",
    },
    {
        "author": "John",
        "date_posted": 10,
        "title": "My Vacation",
        "content": "I just got back from an amazing vacation.",
    },
    {
        "author": "Jane",
        "date_posted": 5,
        "title": "My New Job",
        "content": "I just started a new job and I'm excited.",
    }
]

def home(request):
    context = {
        # "posts": posts,
        "posts": Post.objects.all().order_by('date_posted'),
        "title": "Welcome"
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
