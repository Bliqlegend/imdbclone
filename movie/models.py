from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
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
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, related_name='reviews',on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + "-" + self.movie.name 


