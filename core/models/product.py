import itertools

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    slug = models.SlugField(unique=True, editable=False, blank=True, default="", max_length=5)
    category = models.ManyToManyField(Category, related_name='products')
    name = models.CharField(max_length=255, default='Cartoon Astronaut T-shirt')
    image = models.ImageField(upload_to='products')
    brand_name = models.CharField(max_length=255, default='adidas')
    size = models.ManyToManyField(Size, related_name='sizes')
    description = models.TextField(default='This a shirt made and sold by Emu company limited.')
    price = models.IntegerField(default=80)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def _generate_slug(self):
        value = str(Product.objects.all().count())
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Product.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, (i + 1))
        self.slug = slug_candidate

    def _capitalize(self):
        brand_name = str(self.brand_name).title()
        self.brand_name = brand_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self._generate_slug()
            self._capitalize()
        super().save(*args, **kwargs)

    def get_product_absolute_url(self):
        return reverse('core:product-details', kwargs={'slug': self.slug})

    def get_product_images_url(self):
        product = Product.objects.get(slug=self.slug)
        return ProductImages.objects.filter(product=product)

    def add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={'slug': self.slug})

    def remove_from_cart(self):
        return reverse('core:remove-from-cart', kwargs={'slug': self.slug})


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_gallery', blank=True,
                                null=True)
    image = models.ImageField(upload_to='product-gallery/', blank=True, null=True)


class CartProduct(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    size = models.CharField(max_length=255, default="")

    def get_total_price(self):
        return self.quantity * self.product.price
