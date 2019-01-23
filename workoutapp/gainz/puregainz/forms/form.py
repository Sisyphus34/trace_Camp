from django import forms
from puregainz.models import WeightTraining

class WeightTrainingForm(forms.ModelForm):
    class Meta:
        model = WeightTraining
        fields = ['exercise', 'rep', 'weight']
        