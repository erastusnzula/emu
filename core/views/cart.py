from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import View

from core.models.order import Order
from core.models.product import Product, CartProduct


class Cart(View):
    def post(self, request, slug, *args, **kwargs):
        quantity = self.request.POST.get("quantity")
        size = self.request.POST.get('size')
        product = get_object_or_404(Product, slug=slug)
        order_product, created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
        qs = Order.objects.filter(user=request.user, ordered=False)
        if qs.exists():
            order = qs[0]
            if order.products.filter(product__slug=product.slug).exists():
                order_product.size = f"{order_product.size}, {quantity}-{size}"
                order_product.quantity += int(quantity)
                order_product.save()
                messages.info(request, f'{order_product.quantity} - {order_product.product.name.title()} added to cart.')
                return redirect('core:product-details', slug=slug)
            else:

                order.products.add(order_product)
                order_product.quantity = int(quantity)
                order_product.size = f"{order_product.quantity}-{size}"
                order_product.save()
                messages.info(request, f'{order_product.quantity} - {order_product.product.name.title()} added to cart.')
                return redirect('core:product-details', slug=slug)
        else:
            ordered_date = timezone.now()
            order = Order.objects.create(user=request.user, ordered_date=ordered_date)
            order.products.add(order_product)
            order_product.quantity = int(quantity)
            order_product.size = f"{order_product.quantity}-{size}"
            order_product.save()
            messages.info(request, f'{order_product.quantity} - {order_product.product.name.title()} added to cart.')
            return redirect('core:product-details', slug=slug)
