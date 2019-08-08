from django.shortcuts import render, redirect
from .models import Dong
# Create your views here.
def home(request):
    saves=Dong.objects
    return render(request,'home.html',{'saves':saves})

def submit(request):
    k = Dong()
    k.message = request.GET['message']
    k.name= request.GET['name']
    k.date= request.GET['date']
    k.save()
    return redirect('/')

def delete(request):
    
    Dong.objects.all().delete()
    return redirect('/')