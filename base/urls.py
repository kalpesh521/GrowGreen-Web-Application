from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = [
    path('base/', views.base, name='base'),
]