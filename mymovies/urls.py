"""
URL configuration for mymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views  # Importa tus vistas de la app movies
from django.contrib.auth import views as auth_views


#from movies.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', views.movie_view, name='movie'),
    path('mediconnect/', views.mediconnect_view, name='mediconnect'),  # Ruta para mediconnect.html
    path('registro/', views.registro_view, name='registro'),  # URL para el registro
    path('login/', auth_views.LoginView.as_view(template_name='movies/login.html'), name='login'),
    path('menu/', views.menu_view, name='menu'),  # Redirigir después del login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL para cerrar sesión
]
