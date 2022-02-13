from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product, Rating

def article(request):
    context = {
        "data": {
            "satu": "aasd"
        }
    }
    path = 'index.html'
    return render(request, path,  context)


def add_rating(request):
    context = {
        "data": {
            "satu": "aasd"
        }
    }
    path = 'add_rating.html'
    return render(request, path,  context)


def list_product(request):
    queryset = Product.objects.extra(
        select={
            'rating': 'select AVG(star) from product_rating where product_rating.product_id = product_product.id'
        }
    )

    context = {"data": queryset}
    path = 'list_product.html'
    return render(request, path,  context)
