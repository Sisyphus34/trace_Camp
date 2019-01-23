from django.contrib import admin
from puregainz.models import Workout, WeightTraining, CardioTraining

# Register your models here.
myModels = [Workout, WeightTraining, CardioTraining]
admin.site.register(myModels)
