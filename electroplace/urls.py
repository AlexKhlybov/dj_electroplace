from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path

from mainapp.views import CatalogListView, HomeListView

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^$", HomeListView.as_view(), name="main"),
    re_path(r"^catalog/$", CatalogListView.as_view(), name="catalog"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
