from django.db import models

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    
    description = models.TextField()
    stream = models.CharField(max_length=100)
    img =models.ImageField(upload_to="static/img")
    
