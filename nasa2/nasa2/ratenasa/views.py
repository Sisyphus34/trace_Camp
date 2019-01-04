from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from ratenasa.models import NasaComment
import requests

# Create your views here.
def pick_date(request):
    return HttpResponse(pick_date.html)
    