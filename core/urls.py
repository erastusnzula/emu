from django.urls import path
from core import views

app_name = 'core'
urlpatterns=[
    path('', views.Index.as_view(), name='index'),
    path('shop', views.Shop.as_view(), name='shop'),
    path('blog', views.Blog.as_view(), name='blog'),
    path('about', views.About.as_view(), name='about'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('cart', views.Cart.as_view(), name='cart'),
]