from django.contrib import admin
from django.urls import path

from MyApp.views import index, search_cep  # Substitua 'myapp' pelo nome do seu aplicativo

urlpatterns = [
    path('', index, name='index'),        # Página inicial ou formulário
    path('search_cep/', search_cep, name='search_cep'),  # Endpoint para buscar o CEP
]
