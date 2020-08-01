from django.forms import modelform_factory
from django.shortcuts import render

# Create your views here.
from meetings.models import Meeting, Room


def details(requests, id):
    meeting = Meeting.objects.get(pk=id)
    return render(requests, "meetings/details.html", {"meeting": meeting})


def meeting_list(requests):
    meetings = Meeting.objects.all()
    return render(requests, "meetings/meeting_list.html", {"meeting_list": meetings})


def room_list(requests):
    rooms = Room.objects.all()
    return render(requests, "meetings/room_list.html", {"room_list": rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def add_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            meetings = Meeting.objects.all()
            return render(request, "meetings/meeting_list.html", {"meeting_list": meetings})
    else:
        form = MeetingForm()
        return render(request, "meetings/add_meeting.html", {"form": form})
