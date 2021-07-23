from os import name
from random import sample

from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


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
    name = models.CharField(verbose_name=_("name"), max_length=32, unique=True)
    desc_brands = models.TextField(verbose_name=_("description"), blank=True)
    image = models.ImageField(upload_to=_("images"), blank=True)
    is_active = models.BooleanField(verbose_name="brands_is_active", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name

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
    screen = models.DecimalField(verbose_name="screen", max_digits=3, decimal_places=2, default=0, blank=True)
    sim = models.PositiveIntegerField(verbose_name="sim_qty", default=0, blank=True)
    storage = models.PositiveIntegerField(verbose_name="storage", default=0, blank=True)
    color = models.CharField(verbose_name="color", max_length=128, blank=True)
    quantity = models.PositiveIntegerField(verbose_name="quantity", default=0)

    is_stock = models.BooleanField(verbose_name="product_sale", db_index=True, default=False)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)
    is_new = models.BooleanField(verbose_name="product_new", db_index=True, default=False)

    created_at = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.name} {self.storage} {self.color}"

    @staticmethod
    def get_items():
        return Products.objects.filter(is_active=True, category=2).order_by("category", "name")

    @staticmethod
    def get_stock_products():
        product_stock = Products.objects.filter(is_stock=True)
        stock = sample(list(product_stock), 4)
        return stock

    def delete(self):
        self.is_active = False
        self.save()


class News(models.Model):
    title = models.CharField(verbose_name="title_news", max_length=128)
    subtitle = models.CharField(verbose_name="subtitle_news", max_length=128)
    text = models.TextField(verbose_name="description", blank=True)
    image = models.ImageField(upload_to="news_images", blank=True)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)

    public_date = models.DateTimeField(False, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name_plural = _("News")

    def __str__(self):
        return f"{self.title}"

    def delete(self):
        self.is_active = False
        self.save()


class Benefits(models.Model):
    title = models.CharField(verbose_name="title", max_length=128)
    desc = models.TextField(verbose_name="description", blank=True)

    class Meta:
        verbose_name = _("Advantage")
        verbose_name_plural = _("Benefits")

    def __str__(self):
        return f"{self.title}"


class Contacts(models.Model):
    city = models.CharField(verbose_name="city", max_length=256)
    phone = models.CharField(verbose_name="phone", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    address = models.CharField(verbose_name="address", max_length=512)
    timetable = models.CharField(verbose_name="timetable", max_length=256)

    def __str__(self):
        return f"{self.city}, {self.address}"

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return f"{self.city}"


class PromoSlider(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=256)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    sort_desc = models.CharField(verbose_name=_("sort_desc"), max_length=256)
    image = models.ImageField(upload_to="promo_images", blank=True)
    is_active = models.BooleanField(verbose_name="product_activ", db_index=True, default=True)

    public_date = models.DateTimeField(False, default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = _("Promo")
        verbose_name_plural = _("Promotions")

    def __str__(self):
        return f"{self.name} ({self.public_date})"

    def delete(self):
        self.is_active = False
        self.save()
