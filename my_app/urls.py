from django.urls import path

from my_app import views

urlpatterns = [

    path("home",views.home,name="home"),
    path("",views.index,name="index"),
    path("dash",views.dash,name='dash'),
    path("data",views.gamesdata,name='data'),
    path("table",views.games_view,name="table"),
    path("delete/<int:id>/",views.games_delete,name="delete"),
    path("update/<int:id>/", views.games_update, name="update")

]
