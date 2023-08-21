from django.shortcuts import render

from forms.forms import tee_shirtForm


# Create your views here.

def pantalon(request):
    return render(request, "pantalon.html")


def tee_shirt(request):
    return render(request, "tee_shirt.html")


def chaussures(request):
    return render(request, "chaussures.html")