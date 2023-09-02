from django.shortcuts import render
from django.utils.datetime_safe import datetime


def homePage(request):
    return render(request, "homepage.html")









