from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from .models import Benefits, Brands, Contacts, News, Products, PromoSlider


class HomeListView(ListView):
    model = PromoSlider
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "electroplace"
        context["promo"] = PromoSlider.objects.all()
        context["brands"] = Brands.objects.all().exclude(image__exact="")
        context["top_news"] = News.objects.all().first()
        context["news"] = News.objects.all().exclude(id=context["top_news"].id)
        context["hits"] = Products.get_stock_products()
        context["benefits"] = Benefits.objects.all()[:3]
        context["contact"] = Contacts.objects.first()
        return context


class CatalogListView(ListView):
    model = Products
    paginate_by = 6
    template_name = "mainapp/catalog.html"
    queryset = Products.get_items()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "electroplace"
        context["contact"] = Contacts.objects.first()
        return context
