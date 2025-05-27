from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from goods.models import Product


def catalog(request, category_slug) -> HttpResponse:
    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_object_or_404(Product.objects.filter(category__slug=category_slug))
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
