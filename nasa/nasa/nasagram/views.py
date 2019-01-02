from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from nasagram.models import NasaComment
import requests
from django.shortcuts import redirect
# Create your views here.
def date_selector(request):
    return render(request, 'date_picker.html')

def nasa_detail(request, id):
    nasa_comment = NasaComment.objects.get(id = id)
    return render(request, 'detail_view.html', {'nasa_comment': nasa_comment})

def nasa_create(request):
    if(request.method == "POST"):
        date_string = request.POST.get('date', '2018-01-01')
        print("This is the date string", date_string)
        date = datetime.strptime(date_string, "%Y-%m-%d").date()
        nasa_comment =  NasaComment.objects.create(
            rating = request.POST.get('rating', 0),
            favorite = request.POST.get('favorite', False) == "on",
            comment = request.POST.get('comment_section', ''),
            date = date,
            url = request.POST.get('url', '')
        )

        return redirect(f'/nasa/comment/detail/{nasa_comment.id}')
    elif(request.method == "GET"):
        date = request.GET.get("date_selected", "")
        # This is a parameter 
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"

        # We are doing a get request
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]
        
        #Render the image and form
        return render(request, 'create_comment.html', {'picture': url, 'date': date})
    else:
        return HttpResponse("why have you done this")
    
def nasa_list(request):
    nasa_comments = NasaComment.objects.all()
    return render(request, 'comment_list.html', { 'nasa_comments': nasa_comments })
