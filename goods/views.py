from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404

from goods.models import Product


def catalog(request, category_slug, page=1) -> HttpResponse:
    if category_slug == "all":
        goods = Product.objects.all()
    else:
        goods = get_list_or_404(Product.objects.filter(category__slug=category_slug))

    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)

    context = {
        "title": "Каталог товаров",
        "goods": current_page,
        "slug_url": category_slug,
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug) -> HttpResponse:

    product = Product.objects.get(slug=product_slug)
    context: dict[str, Product] = {
        "product": product,
    }
    return render(request, "goods/product.html", context=context)
