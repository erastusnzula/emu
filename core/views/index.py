from django.shortcuts import render
from django.views import View

from core.models import Feature, Product


class Index(View):
    def get(self, *args, **kwargs):
        features = Feature.get_features()
        products = Product.get_products()
        context = {
            'features': features,
            'products': products,
        }
        return render(self.request, 'index.html', context)
