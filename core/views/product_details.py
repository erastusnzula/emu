from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from core.models.product import Product


class ProductDetails(DetailView):
    model = Product
    template_name = 'product-details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetails,
                        self).get_context_data(**kwargs)
        context["products"] = Product.objects.all()[:4]
        return context
