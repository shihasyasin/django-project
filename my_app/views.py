from django.shortcuts import render

from my_app.forms import gamesForm


# Create your views here.
def home(request):

    return render(request,"views.html")

def index(request):
    return render(request,'index.html')

def dash(request):
    return render(request,"dash.html")

def gamesdata(request):
    form =gamesForm()
    print(form)
    return render(request,'temp.html',{'form':form})