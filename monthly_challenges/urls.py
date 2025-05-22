
from django.urls import path
from . import views
from .constant import MONTH_NAME, LANDING_PAGE

urlpatterns = [
    path('', views.monthly_menu, name=LANDING_PAGE),
    path('<int:month>', views.month_and_goal_view_int),
    path('<str:month>', views.month_and_goal_view, name=MONTH_NAME),
]