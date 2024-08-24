from django import views
from django.urls import include, path

from Pokemon import views
from .views import crud_view, update_pokemon, delete_pokemon, create_pokemon

urlpatterns = [
     path('index/',views.index, name='index'),
   
    path('', crud_view, name='crud_page'),
    path('create/', create_pokemon, name='create_pokemon'),
    path('update/<int:pk>/', update_pokemon, name='update_pokemon'),
    path('delete/<int:pk>/', delete_pokemon, name='delete_pokemon'),
]
