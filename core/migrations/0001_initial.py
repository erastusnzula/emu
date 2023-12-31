# Generated by Django 4.2.6 on 2023-11-05 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='', editable=False, max_length=5, unique=True)),
                ('name', models.CharField(default='Cartoon Astronaut T-shirt', max_length=255)),
                ('image', models.ImageField(upload_to='products')),
                ('brand_name', models.CharField(default='adidas', max_length=255)),
                ('description', models.TextField(default='This a shirt made and sold by Emu company limited.')),
                ('price', models.IntegerField(default=80)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='products', to='core.category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product-gallery/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_gallery', to='core.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(related_name='sizes', to='core.size'),
        ),
    ]
