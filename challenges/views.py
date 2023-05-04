from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


monthly_challenges = {
    "january": "<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>",
    "february": "Workout 5 days a week.",
    "march": "Read 4 books.",
    "april": "Fast for 16 hours each day.",
    "may": "Walk the dogs every weekday.",
    "june": "Workout 5 days a week.",
    "july": "Read 4 books.",
    "august": "Fast for 16 hours each day.",
    "september": "Workout 5 days a week.",
    "october": "Walk the dogs every weekday.",
    "november": "Read 4 books.",
    "december": "Fast for 16 hours each day.",

}

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
    return HttpResponse("<h1 style='text-align: center; color: orange; margin-top:50px;'>Fast for 16 hours each day.</>")


def monthly_challenge(request, month):
    # if month == 'may':
    #     challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>"
    # elif month == 'june':
    #     challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>"
    # elif month == 'july':
    #     challenge_text = "<h1 style='text-align: center; color: green; margin-top:50px;'>Read 4 books.</>"
    # elif month == 'august':
    #     challenge_text = "<h1 style='text-align: center; color: orange; margin-top:50px;'>Fast for 16 hours each day.</>"
    # else:
    #     challenge_text = "<h1 style='text-align: center; color: red; margin-top:50px;'>Not a valid month."
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Please enter a valid month.")
    

#Takes an int and produces the corresponding month in the monthly_challenges dictionary(BROKEN)
def monthly_challenge_by_number(request, month_num):
    months = list(monthly_challenges.keys())
    redirect_month = months[month_num-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)
