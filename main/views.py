from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Category


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Floo Sport - Главная"
        context["content"] = "Магазин спортивного питания Floo Sport"
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "FlooSport - О нас"
        context["content"] = "О нас"
        context["text_on_page"] = "Лучший магазин спортивного питания."
        return context


# def index(request) -> HttpResponse:
#
#     categories = Category.objects.all().order_by("name")
#
#     context: dict[str, str] = {
#         "title": "Floo Sport - Главная",
#         "content": "Магазин спортивного питания Floo Sport",
#     }
#     return render(request, "main/index.html", context)


# def about(request) -> HttpResponse:
#     context: dict[str, str] = {
#         "title": "FlooSport - о нас",
#         "content": "О нас",
#         "text_on_page": "Лучший магазин спортивного питания.",
#     }
#     return render(request, "main/about.html", context)
