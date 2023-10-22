from django.shortcuts import render
from django.views import View
from core.models import Feature, Product


class Index(View):
    def get(self,*args, **kwargs ):
        features = Feature.objects.all()
        products = Product.objects.all()
        context = {
            'features': features,
            'products': products,
        }
        return render(self.request, 'index.html', context)

class Shop(View):
    def get(self, *args, **kwargs):
        features = Feature.objects.all()
        products = Product.objects.all()
        context = {
            'features': features,
            'products': products,
        }
        return render(self.request, 'shop.html', context)
    
class Blog(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog.html')
    
class About(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'about.html')
    
class Contact(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'contact.html')
    
class Cart(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'cart.html')