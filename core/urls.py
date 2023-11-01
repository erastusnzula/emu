from django.urls import path
from core.views import index, shop, cart, contact, about, blog, product_details

app_name = 'core'
urlpatterns = [
    path('', index.Index.as_view(), name='index'),
    path('shop', shop.Shop.as_view(), name='shop'),
    path('<int:product_id>/', product_details.ProductDetails.as_view(), name='product-details'),
    path('blog', blog.Blog.as_view(), name='blog'),
    path('about', about.About.as_view(), name='about'),
    path('contact', contact.Contact.as_view(), name='contact'),
    path('cart', cart.Cart.as_view(), name='cart'),
]
