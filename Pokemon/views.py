from django.shortcuts import redirect, render
import requests
from .models import Pokemon
from .forms import PokemonForm
from django.shortcuts import render, get_object_or_404
from .models import Pokemon

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
            ability = data.get("abilities", [{}])[0].get("ability", {}).get("name", "").capitalize()

            pokemon_info = {
                "name": name,
                "type": type_,
                "image": image,
                "ability": ability,
            }

            context = {'pokemon_info': pokemon_info}
        else:
            context = {'error_message': 'Pokémon não encontrado'}
    else:
        context = {'error_message': 'Por favor, insira um nome de Pokémon válido'}

    return render(request, 'Pokemon/index.html', context)

def update_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    
    if request.method == 'POST':
        # Supondo que você esteja usando um formulário para atualizar
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('crud')  # Redireciona para a página de CRUD após a atualização
    else:
        form = PokemonForm(instance=pokemon)
    
    context = {
        'form': form,
        'pokemon': pokemon
    }
    return render(request, 'Pokemon/update_pokemon.html', context)


def crud_page(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'Pokemon/crud.html', {'pokemons': pokemons})

def create_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = PokemonForm()
    
    return render(request, 'Pokemon/create_pokemon.html', {'form': form})



def delete_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('crud_page')
    return render(request, 'Pokemon/confirm_delete.html', {'pokemon': pokemon})

def delete_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('crud')
    
    return render(request, 'Pokemon/delete_pokemon.html', {'pokemon': pokemon})

def create_pokemon(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        image = request.POST.get("image")
        ability = request.POST.get('ability')

        Pokemon.objects.create(name=name, type=type, ability=ability)
        return redirect('crud')
    return render(request, 'Pokemon/create_pokemon.html')
