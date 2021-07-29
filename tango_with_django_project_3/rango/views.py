from django.shortcuts import render

from django.http import HttpResponse

def home_page(request):
    #Method 1
    html = "Please check the website http://127.0.0.1:8000/index 或 http://127.0.0.1:8000/about！"
    return HttpResponse(html)

def index_views(request):
    #Method 2
    return HttpResponse("Rango says hey there partner!")

def about_views(request):

    return HttpResponse("Rango says here is the about page.")