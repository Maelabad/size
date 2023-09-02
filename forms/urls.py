from django.contrib import admin
from django.urls import path

from forms.views import tee_shirt, chaussures, pantalon
from res.views import response

urlpatterns = [
    path('tee_shirt/', tee_shirt, name="tee_shirt form"),
    path('pantalon/', pantalon, name="pantalon form"),
    path('chaussures/', chaussures, name="chaussures form"),

    #path('<str:categorie_article>/response/', response, name="response"),
]
