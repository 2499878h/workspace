

from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):

    html = "Please check the website http://127.0.0.1:8000/admin/"
    return HttpResponse(html)


def index_html(request):

    return render(request, 'index.html')

def about_html(request):

    return render(request, 'about.html')