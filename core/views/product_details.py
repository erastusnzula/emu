from django.shortcuts import render
from django.views import View

from core.models import Feature, Product


class ProductDetails(View):
    def get(self, request,product_id):
        product = Product.objects.get(id=product_id)
        products = Product.objects.all()[:4]
        context = {
            'product': product,
            'products': products,
        }
        return render(request, 'product-details.html', context)
