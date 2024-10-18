from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    b_author = models.TextField()
    like = models.TextField()
    dislike = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField()
    c_author = models.TextField()
    movieinfos = models.TextField()
