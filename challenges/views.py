from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


monthly_challenges = {
    "january": "Walk the dogs every weekday.",
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


# Home route

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    #index_page = reverse("index", args=[None])
    #print(index_page)

    for month in months:
       month_path = reverse("monthly-challenge", args=[month])
       list_items += f"<li style='list-style-type: none; text-align: center; margin-top: 17px; font-size: 35px;'><a href='{ month_path }' style=' text-decoration: none;'>{ month.capitalize() }</a></li>"
    return HttpResponse(list_items)


# IF "challenges/january"

# def january(request):
#     return HttpResponse("<h1 style='text-align: center; color: red; margin-top:50px;'>Walk the dogs every weekday.</>")


# # IF "challenges/february"

# def february(request):
#     return HttpResponse("<h1 style='text-align: center; color: purple; margin-top:50px;'>Workout 5 days a week.</>")


# # IF "challenges/march"

# def march(request):
#     return HttpResponse("<h1 style='text-align: center; color: green; margin-top:50px;'>Read 4 books.</>")


# # IF "challenges/april" 

# def april(request):
#     return HttpResponse("<h1 style='text-align: center; color: orange; margin-top:50px;'>Fast for 16 hours each day.</>")


# Takes in month and produces the corresponding "challenge_text"

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
    month = month.lower()
    try:
        challenge_text = monthly_challenges[month]
        print(challenge_text)
        response_text = f"<h1 style='text-align: center; color: orange; margin-top:50px;'>{ challenge_text }</h1><br><br><a href='/' style=' text-decoration: none;'>View all months...</a>"
        return HttpResponse(response_text)
    except:
        return HttpResponseNotFound("<h1 style='text-align: center; font-size: 50px; color: Maroon; margin-top:50px;'>Please enter a valid month.</> <br><br> <a href=''></a>")
    

# Takes an int and produces the corresponding month in the monthly_challenges dictionary
#   Rediecting to "monthly_challenge view" OR "january" OR "february" OR "march" OR "April"
#       I know, it's stupid but I'm learning how Django handles the routing by doing this

def monthly_challenge_by_number(request, month_num):
   months = list(monthly_challenges.keys())
   #print(months)
   if month_num > len(months):
    return HttpResponse("Please enter a valid month number (1-12)")
   else:
    redirect_month = months[month_num-1]
    print(redirect_month)
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    print(redirect_path)
    return HttpResponseRedirect(redirect_path)
