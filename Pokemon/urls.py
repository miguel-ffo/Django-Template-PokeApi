from django import views
from django.urls import path
from .views import index, get_pokemon, crud_view, update_pokemon, delete_pokemon, create_pokemon

urlpatterns = [
    path('', index, name='index'),
    path('get_pokemon/', get_pokemon, name='get_pokemon'),
    path('crud/', crud_view, name='crud_page'),
    path('create/', create_pokemon, name='create_pokemon'),
    path('update/<int:pk>/', update_pokemon, name='update_pokemon'),
    path('delete/<int:pk>/', delete_pokemon, name='delete_pokemon'),
]
