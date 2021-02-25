from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from .views import get_sign_to_globe, check

urlpatterns = [    
    path('sign', get_sign_to_globe, name='get_sign'),    
]

if settings.DEBUG:
    urlpatterns.append(path('', check))
