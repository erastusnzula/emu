from django.urls import path
from core.views import index, shop, cart, contact, about, blog, product_details

app_name = 'core'
urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('shop', shop.Shop.as_view(), name='shop'),
    path('<slug:slug>/', product_details.ProductDetails.as_view(), name='product-details'),
    path('blog', blog.Blog.as_view(), name='blog'),
    path('about', about.About.as_view(), name='about'),
    path('contact', contact.Contact.as_view(), name='contact'),
    path('add-to-cart/<slug>/', cart.Cart.as_view(), name='add-to-cart'),
    path('remove-from-cart/<slug>/', cart.remove_from_cart, name='remove-from-cart'),
    path('add-cart-quantity/<slug>/', cart.add_to_cart, name='add-cart-quantity'),
    path('reduce-cart-quantity/<slug>/', cart.reduce_cart_quantity, name='reduce-cart-quantity'),
    path('cart', cart.CartSummary.as_view(), name='cart-summary')
]
