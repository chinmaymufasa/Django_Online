
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
]

