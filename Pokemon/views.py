from django.shortcuts import  render
import requests
from .models import Pokemon




def index(request):
    return render(request, 'Pokemon/index.html')

def get_pokemon(request):
    pokemon_name = request.GET.get('pokemon_name', '').lower()

    if pokemon_name:
        api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            name = data.get("forms", [{}])[0].get("name", "").capitalize()
            type_ = data.get("types", [{}])[0].get("type", {}).get("name", "").capitalize()
            image = data.get("sprites", {}).get("front_default", "N/A")
            image_shiny = data.get("sprites", {}).get("front_shiny", "N/A")
            ability = data.get("abilities", [{}])[0].get("ability", {}).get("name", "").capitalize()

            pokemon_info = {
                "name": name,
                "type": type_,
                "image": image,
                "image_shiny": image_shiny,
                "ability": ability,
            }

            # Atualiza ou cria o Pokémon no banco de dados
            pokemon, created = Pokemon.objects.update_or_create(
                name=pokemon_info['name'],
                defaults=pokemon_info
            )

            context = {'pokemon_info': pokemon_info}
        else:
            context = {'error_message': 'Pokémon não encontrado'}
    else:
        context = {'error_message': 'Por favor, insira um nome de Pokémon válido'}

    return render(request, 'Pokemon/index.html', context)

