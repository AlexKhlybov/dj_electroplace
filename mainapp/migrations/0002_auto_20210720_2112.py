# Generated by Django 2.2.24 on 2021-07-20 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, upload_to="news_images"),
        ),
        migrations.AddField(
            model_name="promoslider",
            name="image",
            field=models.ImageField(blank=True, upload_to="promo_images"),
        ),
    ]
