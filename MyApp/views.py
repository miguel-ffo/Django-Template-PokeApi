from django.http import JsonResponse
from django.shortcuts import render
import requests



def index(request):
    return render(request,'index.html')
# Create your views here.

def search_cep(request):
    cep = None
    if request.method == 'POST':
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        rua = request.POST.get('rua')
    
    url_api = (f'http://www.viacep.com.br/ws/{estado}/{cidade}/{rua}/json')

    try:
        response = request.get(url_api)
        response.raise_for_status()
        data = response.json()

        cep = data.get('cep','CEP não encontrado')
    except requests.RequestException as e:
            cep = f'Erro ao consultar a API: {e}'

    return render(request, 'index.html', {'cep': cep})