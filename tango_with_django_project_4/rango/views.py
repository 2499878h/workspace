

from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    #Method 1
    html = "Please check the website http://127.0.0.1:8000/index 或 http://127.0.0.1:8000/about！"
    return HttpResponse(html)

def index_views(request):
    #Method 2
    return HttpResponse("Rango says hey there partner!")

def about_views(request):

    return HttpResponse("Rango says here is the about page.")

#Method 1
def index_html(request):
    from django.template import loader
    return render(request, 'index.html')
    #t = loader.get_template.rango('index.html')
    #html = t.render()
    #return HttpResponse(html)

#Method 2
def about_html(request):
    from django.shortcuts import render
   # return render(request, 'about.html')