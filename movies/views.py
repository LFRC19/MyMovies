from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Para mostrar mensajes de éxito o error
from django.contrib.auth.decorators import login_required





# Create your views here.
def index(request):
    saludo  = "Hola Mundo"
    return HttpResponse(saludo)
    
def movie_view(request):
    return render(request, 'movies/movie.html')

def mediconnect_view(request):
    return render(request, 'movies/mediconnect.html')
    
def registro_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el usuario en la base de datos
            messages.success(request, "Tu cuenta ha sido creada con éxito. ¡Ya puedes iniciar sesión!")
            return redirect('login')  # Redirige a la URL de login
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserCreationForm()
    
    return render(request, 'movies/registro.html', {'form': form})
    
    
@login_required
def menu_view(request):
    return render(request, 'movies/menu.html')
    
    