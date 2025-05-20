from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

month_goal_dictionary = {
    "january": "Create a yearly budget plan",
    "February": "Improve sleep schedule",
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


def month_and_goal_view_int(request, month):
    uri = list(month_goal_dictionary.keys())[month - 1]
    return HttpResponseRedirect(uri)


def month_and_goal_view(request, month):
    htmlString = month_goal_dictionary[month]
    return HttpResponse(htmlString)
