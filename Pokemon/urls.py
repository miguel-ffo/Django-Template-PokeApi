from django import views
from django.urls import include, path
from .views import index, get_pokemon

urlpatterns = [
    path('', index, name='index'),
    path('get_pokemon/', get_pokemon, name='get_pokemon'),
    path('crud/',include('Crud.urls')),
    
]
