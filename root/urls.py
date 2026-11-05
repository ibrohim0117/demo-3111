from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from apps.views import book_list_view, home_view
from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('books/', book_list_view, name='book_list'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
