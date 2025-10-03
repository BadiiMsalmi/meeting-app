from django.shortcuts import get_object_or_404, render, redirect

from meeting.models import Meeting,Room
from .forms import MeetingForm

# Create your views here.

def detail(request, id):
    print(f"********************************* ID: {id}")
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meeting/detail.html", {"meeting": meeting})

def room_view(request):
    room_data={'rooms': Room.objects.all()}
    return render(request,"meeting/rooms.html",context=room_data)

def new_meeting_view(request):
    if request.method == "POST":
        form = MeetingForm(request.POST) 
        
        if form.is_valid():
            form.save() 
            return redirect('home') 

    else:
        form = MeetingForm()
        
    return render(request, "meeting/new.html", {'form': form})