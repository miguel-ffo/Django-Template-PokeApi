from django.shortcuts import render
import requests
from .models import Pokemon


def index(request):
    return render(request, 'Pokemon/index.html')

def get_pokemon(request):
    pokemon_name = request.GET.get('pokemon_name')

    if pokemon_name:
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(api_url)

        if response.status_code == 200:  # Verifica se a requisição foi bem-sucedida
            data = response.json()
        

        if data['Response'] == True:
            pokemon_info = {
                "name": data['forms'][0]['name'],
                "type": data['type']['name'],
                "image": data['sprites']['front_default'],
            }

            pokemon, created = Pokemon.objects.update_or_create(
                name = pokemon_info["name"],
                defaults = pokemon_info
            )

            context = {'pokemon_info' : pokemon_info}
        else:
            context = {'error_message' :  data.get('Error' , 'Pokemon não encontrado')}
    else:
        context = {'error_message' : 'Por favor insira um nome de pokemon válido'}

        return render(request, 'Pokemon/index.html' , context)


