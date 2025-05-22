from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": 'Home - Главная',
        'content': 'Магазин спортивного питания',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Лушчий магазин спортивного питания.',
    }
    return render(request, 'main/about.html', context)
