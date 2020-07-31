from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from meetings.models import Meeting


def about(requests):
    return HttpResponse('My About US Page')


def contact(requests):
    return HttpResponse('My Contact US Page')


def home(requests):
    return HttpResponse('This is my home page !')


def welcome(requests):
    return render(requests, "website/welcome.html", {"message": "This is welcome message by View methods",
                                                     "num_meetings": Meeting.objects.count()})
