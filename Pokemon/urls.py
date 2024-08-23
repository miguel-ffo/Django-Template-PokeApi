from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('get_pokemon', views.get_pokemon, name="get_pokemon"),
]