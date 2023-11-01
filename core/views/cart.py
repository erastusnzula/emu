from django.shortcuts import render
from django.views import View


class Cart(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'cart.html')
