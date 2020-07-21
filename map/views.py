from django.shortcuts import render

# Create your views here.
def home(request) :
    return render(request, "home.html")

def seunghwa(request) :
    return render(request, "seunghwa.html")

def yeonbeen(request) :
    return render(request, "yeonbeen.html")