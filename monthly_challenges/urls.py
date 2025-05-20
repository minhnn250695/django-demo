
from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>', views.month_and_goal_view_int),
    path('<str:month>', views.month_and_goal_view),
]