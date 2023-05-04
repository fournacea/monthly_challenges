from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1 style='text-align: center; color: blue; margin-top:50px;'>This works!</>")

def january(request):
    return HttpResponse("<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>")

def february(request):
    return HttpResponse("<h1 style='text-align: center; color: purple; margin-top:50px;'>Workout 5 days a week.</>")

def march(request):
    return HttpResponse("<h1 style='text-align: center; color: green; margin-top:50px;'>Read 4 books.</>")

def april(request):
    return HttpResponse("<h1 style='text-align: center; color: orange; margin-top:50px;'>Fast for 16 hours each day</>")

def monthly_challenge(request, month):
    if month == 'may':
        challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>"
    elif month == 'june':
        challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>"
    elif month == 'july':
        challenge_text = "<h1 style='text-align: center; color: green; margin-top:50px;'>Read 4 books.</>"
    elif month == 'august':
        challenge_text = "<h1 style='text-align: center; color: orange; margin-top:50px;'>Fast for 16 hours each day.</>"
    else:
        challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Not a valid month."
    return HttpResponse(challenge_text)