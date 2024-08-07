from django.shortcuts import render, redirect

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
def games_delete(request,id):
    data = games.objects.get(id=id)
    data.delete()
    return redirect("table")
def games_update(request,id):
    data = games.objects.get(id=id)
    form = gamesForm(instance = data)
    if request.method == 'POST':
        data=gamesForm(request.POST,instance=data)
        if data.is_valid():
            data.save()
            return redirect("table")
    return render(request,'update.html',{'form':form})