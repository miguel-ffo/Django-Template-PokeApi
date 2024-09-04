# Projeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('custom_login') if not request.user.is_authenticated else redirect('index')),
    path('admin/', admin.site.urls),
    path('auth/', include('Authentication.urls')),  # Ajuste conforme o nome do seu app de autenticação
    path('pokemon/', include('Pokemon.urls')),  # Inclua as URLs do app Pokémon
]
