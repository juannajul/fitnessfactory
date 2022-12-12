"""Main Url's module"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecommerce/', include(('ecommerce.urls', 'ecommerce'), namespace="ecommercer")),
] 

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
