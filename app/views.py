from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html') 


def agendar(request):
    return render(render, 'app/agendar.html')

def nav(request):
    return render(render, 'app/nav_foot/nav')