from django.shortcuts import render

# Create your views here.
from meetings.models import Meeting


def details(requests, id):
    meeting = Meeting.objects.get(pk=id)
    return render(requests, "meetings/details.html", {"meeting": meeting})


def meeting_list(requests):
    meetings = Meeting.objects.all()
    return render(requests, "meetings/meeting_list.html", {"meeting_list": meetings})
