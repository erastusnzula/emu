from django.shortcuts import render
from django.views import View

from core.models import Feature, Product


class Shop(View):
    def get(self, *args, **kwargs):
        features = Feature.objects.all()
        products = Product.objects.all()
        context = {
            'features': features,
            'products': products,
        }
        return render(self.request, 'shop.html', context)
