from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from  datetime import date 
import random
import string

# Create your views here.

def home(request: HttpRequest):


    return render(request ,"main/home.html")

def today(request: HttpRequest):
    
    day =  date.today()
    context ={"day":day}

    return render(request ,"main/today.html",context)

def random(request: HttpRequest):
     
     
    return render(request ,"main/random.html")

def password(request: HttpRequest):
    
    password = "555555"

    context = {"password": password}

    return render(request ,"main/password.html",context)

def favs(request: HttpRequest):


    return render(request ,"main/favs.html")

def games(request: HttpRequest):
    
    games = ["The Last of Us", "Minecraft", "Resident Evil"]

    context= {"games":games}

    return render(request ,"main/games.html",context)



