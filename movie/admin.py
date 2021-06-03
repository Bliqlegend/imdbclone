from django.contrib import admin
from .models import Movie,StreamPlatforms,Review
# Register your models here.
admin.site.register(Movie)
admin.site.register(StreamPlatforms)
admin.site.register(Review)