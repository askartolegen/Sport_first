from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('boxing/',views.boxing,name='boxing'),
    path('wrestling/',views.wrestling,name='wrestling'),
    path('athletics/',views.athletics,name='athletics'),
    path('weightlifting/',views.weightlifting,name='weightlifting'),
    path('cycling/',views.cycling,name='cycling'),
    path('team_sports/',views.team_sports,name='team_sports'),
]