from os import name
from random import sample

from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone


class ProductsCategory(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=32, unique=True)
    desc_category = models.TextField(verbose_name="Описание", blank=True)
    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()


class Brands(models.Model):
    name = models.CharField(verbose_name="Название", max_length=32, unique=True)
    desc_brands = models.TextField(verbose_name="Описание", blank=True)
    image = models.ImageField(upload_to="Изображение", blank=True)
    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бранды"

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

    name = models.CharField(verbose_name="Продукт", max_length=128)
    image = models.ImageField(upload_to="Изображение", blank=True)
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, default=0)
    old_price = models.DecimalField(verbose_name="Старая цена", max_digits=8, decimal_places=2, default=0, blank=True)
    screen = models.DecimalField(verbose_name="Экран", max_digits=3, decimal_places=2, default=0, blank=True)
    sim = models.PositiveIntegerField(verbose_name="Кол-во сим карт", default=0, blank=True)
    storage = models.PositiveIntegerField(verbose_name="Хранилище", default=0, blank=True)
    color = models.CharField(verbose_name="Цвет", max_length=128, blank=True)
    quantity = models.PositiveIntegerField(verbose_name="Кол-во", default=0)

    is_stock = models.BooleanField(verbose_name="В акции", db_index=True, default=False)
    is_new = models.BooleanField(verbose_name="Новинка", db_index=True, default=False)
    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)

    created_at = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Обновлен", auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

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
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    subtitle = models.CharField(verbose_name="Подзаголовок", max_length=128)
    text = models.TextField(verbose_name="Текст", blank=True)
    image = models.ImageField(upload_to="Изображение", blank=True)
    is_active = models.BooleanField(verbose_name="Активная", db_index=True, default=True)

    public_date = models.DateTimeField(verbose_name="Дата публикации",  default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return f"{self.title}"

    def delete(self):
        self.is_active = False
        self.save()


class Benefits(models.Model):
    title = models.CharField(verbose_name="Заголовок", max_length=128)
    desc = models.TextField(verbose_name="Текст", blank=True)

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return f"{self.title}"


class Contacts(models.Model):
    city = models.CharField(verbose_name="Город", max_length=256)
    phone = models.CharField(verbose_name="Телефон", max_length=20)
    email = models.CharField(verbose_name="e-mail", max_length=128)
    address = models.CharField(verbose_name="Адрес", max_length=512)
    timetable = models.CharField(verbose_name="Часы работы", max_length=256)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.city}, {self.address}"


class PromoSlider(models.Model):
    name = models.CharField(verbose_name="Название", max_length=256)
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    sort_desc = models.CharField(verbose_name="Короткое описание", max_length=256)
    image = models.ImageField(upload_to="Изображение", blank=True)
    is_active = models.BooleanField(verbose_name="Активный", db_index=True, default=True)

    public_date = models.DateTimeField(verbose_name="Дата публикации", default=timezone.now)
    updated_at = models.DateTimeField(verbose_name="Обновлено", auto_now=True)

    class Meta:
        verbose_name = "Акция слайд"
        verbose_name_plural = "Акции слайд"

    def __str__(self):
        return f"{self.name} ({self.public_date})"

    def delete(self):
        self.is_active = False
        self.save()
