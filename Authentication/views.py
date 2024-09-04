from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para a função index
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'Pokemon/login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if not User.objects.filter(username=email).exists():
                # Criar um superusuário
                User.objects.create_superuser(username=email, email=email, password=password, first_name=name)
                return redirect('custom_login')
            else:
                # O usuário já existe
                return render(request, 'Pokemon/register.html', {'error': 'User already exists'})
        else:
            # Senhas não coincidem
            return render(request, 'Pokemon/register.html', {'error': 'Passwords do not match'})

    return render(request, 'Pokemon/register.html')