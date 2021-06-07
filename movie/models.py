from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Upcoming(models.Model):
    name = models.CharField(max_length=244)
    url = models.URLField(max_length=255)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StreamPlatforms(models.Model):
    name = models.CharField(max_length=30)
    aboutype = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.name




class Movie(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=False,blank=True)
    platform = models.ForeignKey(StreamPlatforms,on_delete=models.CASCADE,related_name="movies")
    description = models.CharField(max_length=255)
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, related_name='reviews',on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + "-" + self.movie.name 



class Genre(models.Model):
    name = models.CharField(max_length=255) 
    movies = models.ForeignKey(Movie,related_name="genres",on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
