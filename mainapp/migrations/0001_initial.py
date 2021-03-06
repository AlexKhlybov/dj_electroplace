# Generated by Django 2.2.24 on 2021-07-20 20:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Benefits",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=128, verbose_name="name")),
                ("desc", models.TextField(blank=True, verbose_name="description")),
            ],
        ),
        migrations.CreateModel(
            name="Brands",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=32, unique=True, verbose_name="brands_name")),
                ("desc_brands", models.TextField(blank=True, verbose_name="brands_desc")),
                ("image", models.ImageField(blank=True, upload_to="brands_images")),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="brands_is_active")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
            ],
        ),
        migrations.CreateModel(
            name="Contacts",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("city", models.CharField(max_length=256, verbose_name="city")),
                ("phone", models.CharField(max_length=20, verbose_name="phone")),
                ("email", models.CharField(max_length=128, verbose_name="e-mail")),
                ("address", models.CharField(max_length=512, verbose_name="address")),
                ("timetable", models.CharField(max_length=256, verbose_name="timetable")),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=128, verbose_name="title_news")),
                ("subtitle", models.CharField(max_length=128, verbose_name="subtitle_news")),
                ("text", models.TextField(blank=True, verbose_name="description")),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="product_activ")),
                ("public_date", models.DateTimeField(default=django.utils.timezone.now, verbose_name=False)),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
            ],
        ),
        migrations.CreateModel(
            name="ProductsCategory",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=32, unique=True, verbose_name="name_category")),
                ("desc_category", models.TextField(blank=True, verbose_name="description")),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="category_is_active")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
            ],
        ),
        migrations.CreateModel(
            name="PromoSlider",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256, verbose_name="name")),
                ("sort_desc", models.CharField(max_length=256, verbose_name="sort_desc")),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="product_activ")),
                ("public_date", models.DateTimeField(default=django.utils.timezone.now, verbose_name=False)),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
                ("brand", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.Brands")),
            ],
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, verbose_name="product")),
                ("image", models.ImageField(blank=True, upload_to="product_images")),
                ("price", models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name="price")),
                (
                    "old_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, default=0, max_digits=8, verbose_name="old_price"
                    ),
                ),
                ("screen", models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name="screen")),
                ("sim", models.PositiveIntegerField(default=0, verbose_name="sim_qty")),
                ("storage", models.PositiveIntegerField(default=0, verbose_name="storage")),
                ("color", models.CharField(max_length=128, verbose_name="color")),
                ("quantity", models.PositiveIntegerField(default=0, verbose_name="quantity")),
                ("is_stock", models.BooleanField(db_index=True, default=False, verbose_name="product_sale")),
                ("is_active", models.BooleanField(db_index=True, default=True, verbose_name="product_activ")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated")),
                ("brands", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.Brands")),
                (
                    "category",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="mainapp.ProductsCategory"),
                ),
            ],
        ),
    ]
