from django.shortcuts import render

from my_app.forms import gamesForm
from my_app.models import games


# Create your views here.
def home(request):

    return render(request,"views.html")

def index(request):
    return render(request,'index.html')

def dash(request):
    return render(request,"dash.html")

def gamesdata(request):
    form =gamesForm()
    if request.method == 'POST':
        data=gamesForm(request.POST)
        if data.is_valid():
            data.save()

    return render(request,'temp.html',{'form':form})

def  games_view(request):
    data = games.objects.all()
    return render(request, 'view_data.html' , {'data': data})