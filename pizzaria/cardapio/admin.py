from django.contrib import admin
from django.utils.html import format_html
from .models import TipoPizza, TipoIngrediente, Ingrediente, Pizza, IngredientePizza

# Register your models here.

@admin.register(TipoPizza)
class TipoPizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(TipoIngrediente)
class TipoIngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'icone']

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_ingrediente', 'preco_unidade', 'unidade_medida', 'disponivel']
    list_filter = ['tipo_ingrediente', 'disponivel']
    
    def preco_formatado(self, obj):
        return f"R$ {obj.preco_por_unidade:.2f}/{obj.unidade_medida}"

    # Rótulo
    preco_formatado.short_description = "Preço"

class IngredientePizzaInline(admin.TabularInline):
    model = IngredientePizza
    extra = 1

    fields = ['ingrediente', 'quantidade_numerica', 'quantidade_texto']

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo_pizza', 'tempo_preparo', 'preco_total_formatado', 'ativa']
    list_filter = ['tipo_pizza', 'ativa']
    inlines = [IngredientePizzaInline]

    def preco_total_formatado(self, obj):
        return f"R$ {obj.preco_total:.2f}"

    preco_total_formatado.short_description = "Preço Total"
