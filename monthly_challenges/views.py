from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .constant import MONTH_NAME
month_goal_dictionary = {
    "january": "Create a yearly budget plan",
    "february": "Improve sleep schedule",
    "march": "Spring clean home and digital devices",
    "april": "Update resume and professional profiles",
    "may": "Schedule annual health checkups",
    "june": "Review half-year accomplishments",
    "july": "Schedule quality time with family and friends",
    "august": "Try a new healthy recipe each week",
    "september": "Set Q4 objectives and priorities",
    "october": "Practice daily mental health habits",
    "november": "Review annual achievements",
    "december": "Reflect and set vision for next year"
}

# Create your views here.

def monthly_menu(request):
    months = list(month_goal_dictionary.keys())
    innerHtml = ""
    for month in months:
        innerHtml += f"<li><a href='{reverse(MONTH_NAME, args=[month])}'>{month.capitalize()}</a></li>"
            
    data_response = f"<ul>{innerHtml}</ul>"
    
    return HttpResponse(data_response)


def month_and_goal_view_int(request, month):
    
    months = list(month_goal_dictionary.keys())
    if month > len(months):
        return HttpResponseRedirect('not-found'); 
    uri = reverse(MONTH_NAME, args= [months[month - 1]])
    return HttpResponseRedirect(uri)


def month_and_goal_view(request, month):
    try:
        htmlString = month_goal_dictionary[month]
    except:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(htmlString)
