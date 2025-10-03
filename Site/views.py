from django.shortcuts import render

from meeting.models import Meeting

# Create your views here.

def home_view(request):
    count={'nbre_meeting': Meeting.objects.count()}
    meetings_data ={'meetings': Meeting.objects.all()}
    context = {**count, **meetings_data}

    return render(request,"site/home.html",context)

def about_view(request):
    return render(request,"site/about.html")