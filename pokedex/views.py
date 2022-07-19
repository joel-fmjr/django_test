from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import *


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'pokedex/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pokedex')


class RegisterPage(FormView):
    template_name = 'pokedex/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pokedex')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pokedex')
        return super(RegisterPage, self).get(*args, **kwargs)


class PokemonList(LoginRequiredMixin, ListView):
    model = Pokemon
    context_object_name = 'pokemons'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokedex'] = Pokedex.objects.filter(user=self.request.user)
        context['pokemons'] = context['pokemons'].filter(pokedex__user=self.request.user)
        return context


class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'species', 'types', 'height', 'weight', 'is_favorite']
    success_url = reverse_lazy('pokedex')

    def form_valid(self, form):
        form.instance.pokedex = Pokedex.objects.get(user=self.request.user) 
        return super(PokemonCreate, self).form_valid(form)


class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['name', 'species', 'types', 'height', 'weight']
    success_url = reverse_lazy('pokedex')


class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    context_object_name = 'pokemon'
    success_url = reverse_lazy('pokedex')


class PokedexCreate(LoginRequiredMixin, CreateView):
    model = Pokedex
    fields = []
    success_url = reverse_lazy('pokedex')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PokedexCreate, self).form_valid(form)