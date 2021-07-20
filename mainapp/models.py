from os import name
from random import sample

from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class ProductsCategory(models.Model):
    name = models.CharField(verbose_name="name_category", max_length=32, unique=True)
    desc_category = models.TextField(verbose_name="description", blank=True)
    is_active = models.BooleanField(verbose_name="category_is_active", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return self.name
    
    def delete(self):
        self.is_active = False
        self.save()


class Brands(models.Model):
    name = models.CharField(verbose_name="brands_name", max_length=32, unique=True)
    desc_brands = models.TextField(verbose_name="brands_desc", blank=True)
    image = models.ImageField(upload_to="brands_images", blank=True)
    is_active = models.BooleanField(verbose_name="brands_is_active", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    @staticmethod
    def get_item(pk):
        return get_object_or_404(Brands, pk=pk)

    def delete(self):
        self.is_active = False
        self.save()


class Products(models.Model):
    category = models.ForeignKey(ProductsCategory, on_delete=models.CASCADE)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)

    name = models.CharField(verbose_name="product", max_length=128)
    image = models.ImageField(upload_to="product_images", blank=True)
    price = models.DecimalField(verbose_name="price", max_digits=8, decimal_places=2, default=0)
    old_price = models.DecimalField(verbose_name="old_price", max_digits=8, decimal_places=2, default=0, blank=True)
    screen = models.DecimalField(verbose_name="screen", max_digits=3, decimal_places=2, default=0)
    sim = models.PositiveIntegerField(verbose_name="sim_qty", default=0)
    storage = models.PositiveIntegerField(verbose_name="storage", default=0)
    color = models.CharField(verbose_name="color", max_length=128)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)

    is_stock = models.BooleanField(verbose_name="product_sale", db_index=True, default=False)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return f"{self.name} {self.storage} {self.color}"

    @staticmethod
    def get_items():
        return Products.objects.filter(is_active=True).order_by("category", "name")

    @property
    def get_stock_products():
        product_stock = Products.objects.filter(is_stock=True)
        return sample(list(product_stock), 4)

    def delete(self):
        self.is_active = False
        self.save()


class News(models.Model):
    title = models.CharField(verbose_name="title_news", max_length=128)
    subtitle = models.CharField(verbose_name="subtitle_news", max_length=128)
    text = models.TextField(verbose_name="description", blank=True)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)

    public_date = models.DateTimeField(False, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def delete(self):
        self.is_active = False
        self.save()


class Benefits(models.Model):
    title = models.CharField(verbose_name="name", max_length=128)
    desc = models.TextField(verbose_name="description", blank=True)


class Contacts(models.Model):
    city = models.CharField(verbose_name="city", max_length=256)
    phone = models.CharField(verbose_name="phone", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    address = models.CharField(verbose_name="address", max_length=512)
    timetable = models.CharField(verbose_name="timetable", max_length=256)

    def __str__(self):
        return f"{self.city}, {self.address}"


class PromoSlider(models.Model):
    name = models.CharField(verbose_name="name", max_length=256)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    sort_desc = models.CharField(verbose_name="sort_desc", max_length=256)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)

    public_date = models.DateTimeField(False, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    def delete(self):
        self.is_active = False
        self.save()