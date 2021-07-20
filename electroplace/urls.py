from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from mainapp.views import main, HomePage, catalog

urlpatterns =[
    path("admin/", admin.site.urls),
    path("", HomePage.as_view(), name="main"),
    path("catalog/", catalog, name="catalog"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
