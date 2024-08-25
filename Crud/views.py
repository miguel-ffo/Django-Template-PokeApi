from django.shortcuts import get_object_or_404, redirect, render
from Pokemon.models import Pokemon
from .forms import PokemonForm

def crud_view(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'Crud/crud.html', {'pokemons': pokemons})

def update_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    
    if request.method == 'POST':
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('crud_page')  
    else:
        form = PokemonForm(instance=pokemon)
    
    context = {
        'form': form,
        'pokemon': pokemon
    }
    return render(request, 'Crud/update_pokemon.html', context)

def create_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud_page')  
    else:
        form = PokemonForm()
    
    return render(request, 'Crud/create_pokemon.html', {'form': form})

def delete_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('crud_page')  
    
    return render(request, 'Crud/delete_pokemon.html', {'pokemon': pokemon})
