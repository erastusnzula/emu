from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
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
                messages.info(request,
                              f'{order_product.quantity} - {order_product.product.name.title()} added to cart.')
                return redirect('core:product-details', slug=slug)
            else:

                order.products.add(order_product)
                order_product.quantity = int(quantity)
                order_product.size = f"{order_product.quantity}-{size}"
                order_product.save()
                messages.info(request,
                              f'{order_product.quantity} - {order_product.product.name.title()} added to cart.')
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

def add_to_cart(request, slug):
    """Adjust an item's quantity positively (cart summary option + )."""
    product = get_object_or_404(Product, slug=slug)
    order_product, created = CartProduct.objects.get_or_create(product=product, user=request.user, ordered=False)
    qs = Order.objects.filter(user=request.user, ordered=False)
    if qs.exists():
        order = qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product.quantity += 1
            order_product.save()
            messages.info(request, f'{order_product.product.name.title()} quantity updated successfully.')
            return redirect('core:cart-summary')
        else:
            order.products.add(order_product)
            messages.info(request, f'{order_product.product.name.title()} added to cart successfully.')
            return redirect('src:cart-summary')
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.products.add(order_product)
        messages.info(request, f'{order_product.product.name.title()} added to cart successfully.')
        return redirect('src:cart-summary')

def reduce_cart_quantity(request, slug):
    """Adjust cart product negatively quantity (-)"""
    product = get_object_or_404(Product, slug=slug)
    qs = Order.objects.filter(user=request.user, ordered=False)
    if qs.exists():
        order = qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product = CartProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            if order_product.quantity > 1:
                order_product.quantity -= 1
                order_product.save()

            else:
                order.products.remove(order_product)
            messages.info(request, f'{order_product.product.name.title()} quantity updated successfully.')
            return redirect('core:cart-summary')
        else:
            messages.warning(request, f'{request.user.username.title()}, this product not in your cart!')
            return redirect('core:product-details', slug=slug)
    else:
        messages.warning(request,
                         f'{request.user.username.title()}, you do not have an active order consider placing one.')
        return redirect('core:product-details', slug=slug)
def remove_from_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    qs = Order.objects.filter(user=request.user, ordered=False)
    if qs.exists():
        order = qs[0]
        if order.products.filter(product__slug=product.slug).exists():
            order_product = CartProduct.objects.filter(product=product, user=request.user, ordered=False)[0]
            order.products.remove(order_product)
            messages.info(request, f'{order_product.product.name.title()} removed from cart successfully.')
            return redirect('core:cart-summary')
        else:
            messages.warning(request, f'{request.user.username.title()}, this product is not in your cart!')
            return redirect('core:product-details', slug=slug)
    else:
        messages.warning(request,
                         f'{request.user.username.title()}, you do not have an active order, consider placing one.')
        return redirect('src:product-details', slug=slug)


class CartSummary(View):
    def get(self, *args, **kwargs):
        try:
            orders = Order.objects.filter(user=self.request.user, ordered=False)
            context = {'orders': orders}
            return render(self.request, 'cart_summary.html', context)
        except ObjectDoesNotExist:
            redirect('core:index')
