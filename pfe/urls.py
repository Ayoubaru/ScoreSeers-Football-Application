from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news', views.news, name="news"),
    path('matches', views.matches, name="matches"),
    path('scores', views.scores, name="scores"),
    path('standings', views.standings, name="standings"),
    path('teamstats', views.teamstats, name="teamstats"),
    path('playerstats', views.playerstats, name="playerstats"),
    path('get_pronostic', views.get_pronostic, name="get_pronostic"),
    path('get_predictions', views.get_predictions, name="get_predictions"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('logoutUser', views.logoutUser, name="logoutUser"),
    path('registerpage', views.registerpage, name="registerpage"),
    path('userprofil', views.userprofil, name="userprofil"),
]
