from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('pokedex', PokemonList.as_view(), name='pokedex'),
    path('pokemon-register/', PokemonCreate.as_view(), name='pokemon-register'),
    path('pokemon-details/<int:pk>/', PokemonDetail.as_view(), name='pokemon-details'),
    path('pokemon-update/<int:pk>/', PokemonUpdate.as_view(), name='pokemon-update'),
    path('pokemon-delete/<int:pk>/', PokemonDelete.as_view(), name='pokemon-delete'),

]