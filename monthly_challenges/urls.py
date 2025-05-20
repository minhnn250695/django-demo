
from django.urls import path
from . import views
from .constant import MONTH_NAME

urlpatterns = [
    path('', views.monthly_menu),
    path('<int:month>', views.month_and_goal_view_int),
    path('<str:month>', views.month_and_goal_view, name=MONTH_NAME),
]