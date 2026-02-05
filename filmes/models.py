from django.db import models

class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='streaming_icons/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    rating = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    streams = models.ManyToManyField(StreamingPlatform, related_name='movies')
    
    def __str__(self):
        return self.title
