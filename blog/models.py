from django.db import models
from django.utils import timezone       # For updating time 
from django.contrib.auth.models import User         # For establishing relationship between post and user

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #  to return the name of blog
    def __str__(self):
        return self.title