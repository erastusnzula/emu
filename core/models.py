from django.db import models


class Feature(models.Model):
    title = models.CharField(max_length=255, default='Feature')
    image = models.ImageField(upload_to='features')
    background_color = models.CharField(max_length=255, default='#fdddef')

    @staticmethod
    def get_features():
        return Feature.objects.all()


class Product(models.Model):
    image = models.ImageField(upload_to='products')
    brand_name = models.CharField(max_length=255, default='adidas')
    title = models.CharField(max_length=255, default='Cartoon Astronaut T-shirt')
    price = models.IntegerField(default=80)

    @staticmethod
    def get_products():
        return Product.objects.all()
