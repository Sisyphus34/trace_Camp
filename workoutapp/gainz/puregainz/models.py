from django.db import models
from django.urls import reverse_lazy



# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
            return f'{self.date}, {self.name}'

    def get_absolute_url(self):
        return reverse_lazy("workout_detail", args = [str(self.id)])

class WeightTraining(models.Model):
    exercises = (
        ('dl', 'Deadlift'),
        ('sq', 'Squat'),
        ('bp', 'Benchpress'),
        ('pd', 'Pulldown'),
        ('rw', 'Row'),
    )
    exercise = models.CharField(max_length=2, blank=True, choices=exercises)
    rep = models.IntegerField(blank=True)
    weight = models.FloatField(blank=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workoutChild")

    #covert object to string for readablity
    def __str__(self):
        return f'{self.exercise} , {self.rep}, {self.weight}'

    
class CardioTraining(models.Model):
    treadmill_time = models.TimeField()
    treadmill_speed = models.FloatField()
    treadmill_distance = models.FloatField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)



