

from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)


def home_page(request):

    html = "Please check the website http://127.0.0.1:8000/admin/ or http://127.0.0.1:8000/index_html"
    return HttpResponse(html)


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'index.html', context=context_dict)


def about_html(request):

    return render(request, 'about.html')