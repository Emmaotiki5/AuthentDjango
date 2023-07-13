from django.db import models
from datetime import datetime


# Initialize AniKimi class

# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    

    
    
