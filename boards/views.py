from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def about(requests):
    return HttpResponse('My About US Page')


def contact(requests):
    return HttpResponse('My Contact US Page')


def home(requests):
    return HttpResponse('This is my home page !')
