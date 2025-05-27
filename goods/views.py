from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Product


def catalog(request) -> HttpResponse:
    goods = Product.objects.all()
    context = {
        "title": "Каталог товаров",
        "goods": goods,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug) -> HttpResponse:

    product = Product.objects.get(slug=product_slug)
    context: dict[str, Product] = {
        "product": product,
    }
    return render(request, "goods/product.html", context=context)
