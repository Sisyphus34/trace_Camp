from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import KickStarter
from django.core import serializers

# Create your views here.
def myapp_view(request, myapp_id):
    kick = KickStarter.objects.filter(id = myapp_id)
    data = serializers.serialize("json", kick)
    return HttpResponse(data)