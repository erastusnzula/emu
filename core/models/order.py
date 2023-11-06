from django.conf import settings
from django.db import models

from core.models.product import CartProduct


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=50, null=True, blank=True)
    products = models.ManyToManyField(CartProduct)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    # billing_address = models.ForeignKey('Address', related_name="billing_address", on_delete=models.SET_NULL,
    #                                     blank=True, null=True)
    # shipping_address = models.ForeignKey('Address', related_name="shipping_address", on_delete=models.SET_NULL,
    #                                      blank=True, null=True)
    # payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)
    # coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)
    ip = models.CharField(max_length=200, default="")

    def get_order_total(self):
        total = 0
        for order in self.products.all():
            total += order.get_total_price()
        return total
