from django.contrib import admin
from django.urls import path
from django_telethon.urls import django_telethon_urls

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('telegram/', django_telethon_urls())
]
