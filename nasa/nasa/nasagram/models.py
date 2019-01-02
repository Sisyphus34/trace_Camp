from django.db import models

# Create your models here.
class NasaComment(models.Model):
    date = models.DateField()
    rating = models.IntegerField()
    comment = models.TextField()
    url = models.URLField()
    favorite = models.BooleanField()
