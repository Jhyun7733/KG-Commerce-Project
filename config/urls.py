
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('acc/',include('acc.urls')),
    path('product/', include("product.urls")),
    path('live/', include("live.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
