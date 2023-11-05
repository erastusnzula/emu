from django.shortcuts import render
from django.views.generic import ListView

from core.models.product import Product


class Shop(ListView):
    model = Product
    template_name = 'shop.html'
