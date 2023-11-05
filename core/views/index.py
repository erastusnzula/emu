from django.shortcuts import render
from django.views.generic import ListView

from core.models.product import Product


class Index(ListView):
    model = Product
    template_name = 'index.html'

