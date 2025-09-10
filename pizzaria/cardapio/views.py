from django.shortcuts import render
from .models import TipoPizza, TipoIngrediente, Ingrediente, Pizza, IngredientePizza   

# Create your views here.

def home(request):
    """Página Inicial"""
    pizzas_salgadas = Pizza.objects.filter(tipo_pizza__nome='Salgada', ativa=True)
    pizzas_doces = Pizza.objects.filter(tipo_pizza__nome='Doce', ativa=True)

    # Dicionario com os dados que eu quero mostrar na tela
    context = {
        
        "pizzas_salgadas": pizzas_salgadas,
        "pizzas_doces": pizzas_doces
    }

    # Renderizar - mostrar na tela
    return render(request, 'cardapio/home.html', context)
