from django.contrib import admin

from .models import Products, ProductsCategory, Brands, News, Benefits, Contacts, PromoSlider

admin.site.register(ProductsCategory)
admin.site.register(Products)
admin.site.register(Brands)
admin.site.register(News)
admin.site.register(Benefits)
admin.site.register(Contacts)
admin.site.register(PromoSlider)
