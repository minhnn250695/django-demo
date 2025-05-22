from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .constant import MONTH_NAME, month_goal_dictionary
from django.template.loader import render_to_string


# Create your views here.

def monthly_menu(request):    
    months = list(month_goal_dictionary.keys())
    return HttpResponse(render(request, 'monthly_challenges/monthly_challenges.html',
    {
        'months': months,
        'name': MONTH_NAME 
    }))

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
