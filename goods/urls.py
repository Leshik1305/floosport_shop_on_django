from django.urls import path
from django.urls.resolvers import URLPattern

from goods import views

app_name = "goods"

urlpatterns: list[URLPattern] = [
    path("", views.catalog, name="index"),
    path("product/", views.product, name="product"),
    path("product/<slug:product_slug>/", views.product, name="product"),
]
