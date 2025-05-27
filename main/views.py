from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category


def index(request) -> HttpResponse:

    categories = Category.objects.all().order_by("name")

    context: dict[str, str] = {
        "title": "Home - Главная",
        "content": "Магазин спортивного питания",
    }
    return render(request, "main/index.html", context)


def about(request) -> HttpResponse:
    context: dict[str, str] = {
        "title": "Home - о нас",
        "content": "О нас",
        "text_on_page": "Лучший магазин спортивного питания.",
    }
    return render(request, "main/about.html", context)
