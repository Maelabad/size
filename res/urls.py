
from django.contrib import admin
from django.urls import path

from res.views import response

urlpatterns = [
    path('response/', response, name="Response page"),

    #path('<str:categorie_article>/response/', response, name="response"),
]
