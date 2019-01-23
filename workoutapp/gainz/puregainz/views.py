from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, TemplateView, UpdateView
from django.http import HttpResponse
from datetime import datetime
from puregainz.models import Workout, WeightTraining
import requests
from django.shortcuts import redirect
from django import forms
from django.forms import formset_factory
from django.urls import reverse_lazy

# Create your views here.
    
class WorkoutListView(ListView):
    model = Workout

class WorkoutUpdateView(UpdateView):
    model = Workout
    fields = ["name", "date"]
    template_name = 'puregainz/workout_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise_list'] = WeightTraining.exercises
            
        return context

    def form_valid(self, form):
        workout = form.save()
        print("THIS IS THE POST a!", self.request.POST)
        ob = self.request.POST 
        # for exercise in WeightTraining.exercises:
        #     if(self.request.POST.get(exercise[0], False) == "on"):
        #         print("Hello asshole!" , exercise)
        #         self.request.POST.get('{exercise[0]}_weight')
        #         WeightTraining.objects.create(
        #             exercise = exercise[0], 
        #             rep = self.request.POST.get(f'{exercise[0]}-rep'),
        #             weight = self.request.POST.get(f'{exercise[0]}-weight'),
        #             workout = workout
        #         )
        return redirect('workout_detail', test = ob, pk = workout.id) # TODO Make this work


class WorkoutDeleteView(DeleteView):
    model = Workout
    success_url = reverse_lazy('workout_list')

class WorkoutDetailView(DetailView):
    model = Workout
    template_name = 'puregainz/workout_detail.html'



class WorkoutCreateView(CreateView):
    model = Workout
    fields = ["date", "name"]
    template_name = 'puregainz/create_gainz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercise_list'] = WeightTraining.exercises
        return context

    def form_valid(self, form):
        workout = form.save()
        print("THIS IS THE POST!", self.request.POST)
        for exercise in WeightTraining.exercises:
            if(self.request.POST.get(exercise[0], False) == "on"):
                print("Hello asshole!" , exercise)
                self.request.POST.get('{exercise[0]}_weight')
                WeightTraining.objects.create(
                    exercise = exercise[0], 
                    rep = self.request.POST.get(f'{exercise[0]}-rep'),
                    weight = self.request.POST.get(f'{exercise[0]}-weight'),
                    workout = workout
                )
        return redirect('workout_detail', pk = workout.id) # TODO Make this work
