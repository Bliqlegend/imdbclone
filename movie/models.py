from django.db import models

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
    description = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name