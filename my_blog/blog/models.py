from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    #Title field of with type CharField of length 255, to store the tittle of blogpost
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #For the built-in user model, to store the author of blogpost
    created_at=models.DateTimeField(auto_now_add=True)
    #Datetime Field to set the current time when the blog post is created
    
    def __str__(self):
        return self.title
    #This method helps to return the string representation of the blog post


# Create your models here.
