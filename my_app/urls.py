from django.urls import path

from my_app import views

urlpatterns = [

    path("home",views.home,name="home") ,
    path("",views.index,name="index") ,
    path("dash",views.dash,name='dash'),
    path("data",views.gamesdata,name='data') ,
    path("table",views.games_view,name="table")

]
