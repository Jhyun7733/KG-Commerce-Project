
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('acc/',include('acc.urls')),
    path('product/', include("product.urls")),
    path('live/', include("live.urls")),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

