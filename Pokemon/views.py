from django.shortcuts import redirect, render, get_object_or_404
import requests
from .models import Pokemon
from .forms import PokemonForm

def crud_view(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'Pokemon/crud.html', {'pokemons': pokemons})

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

def update_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('crud_page')  # Corrigido para 'crud_page'
    else:
        form = PokemonForm(instance=pokemon)
    
    context = {
        'form': form,
        'pokemon': pokemon
    }
    return render(request, 'Pokemon/update_pokemon.html', context)

def create_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_page')  # Corrigido para 'crud_page'
    else:
        form = PokemonForm()
    
    return render(request, 'Pokemon/create_pokemon.html', {'form': form})

def delete_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('crud_page')  # Corrigido para 'crud_page'
    
    return render(request, 'Pokemon/delete_pokemon.html', {'pokemon': pokemon})
