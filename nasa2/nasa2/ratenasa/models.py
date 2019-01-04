from django.db import models

# Create your models here.
class NasaComment():
    comment = models.TextField()
    rating  = models.IntegerField(range(1,6))
    date = models.DateField()
    favorite = models.BooleanField()
    