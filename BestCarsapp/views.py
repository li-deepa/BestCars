from django.shortcuts import render

# Create your views here.

def home(request):
    context={}
    return render(request,"BestCarsapp/home.html",context)

def contact(request):
    context={}
    return render(request,"BestCarsapp/contactus.html",context)

def about(request):
    context={}
    return render(request,"BestCarsapp/aboutus.html",context)
