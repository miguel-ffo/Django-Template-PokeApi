from django.shortcuts import render
import requests
from .models import Pokemon


def index(request):
    return render(request, 'Pokemon/index.html')


