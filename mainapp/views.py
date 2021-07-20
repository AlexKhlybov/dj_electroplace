from django.shortcuts import render
from django.views.generic import ListView

from .models import Brands, PromoSlider


class HomePage(ListView):
    model = PromoSlider
    template_name = 'mainapp/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['promo'] = PromoSlider.objects.all()
        context['brands'] = Brands.objects.all().exclude(image__exact='')
        return context



def main(request):
    return render(request, "mainapp/index.html")


def catalog(request):
    return render(request, "mainapp/catalog.html")


def contact(request):
    pass