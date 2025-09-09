from django.db import models

# Create your models here.

class TipoPizza(models.Model):
    nome = models.CharField(max_length=50) #Charfield - Texto Curto
    descicao = models.TextField(blank=True) #TextoField - Texto Longo
    cor_hex = models.CharField(max_length=7, default="#FF6B6")

    def __str__(self):
        return self.nome

class TipoIngrediente(models.Model):
    nome = models.Charfield(max_length=100)
    icone = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    tipo_ingrediente = models.ForeignKey(TipoIngrediente,on_delete=models.CASCADE)
    preco_unidade = models.DecimalField(max_digits=8, decimal_places=3, default=0.000)
    unidade_medida = models.CharField(max_length=20, default='g')
    disponivel = models.BooleanField(defauld=True)

    def __str__(self):
        return f"{self.nome} - R${self.peco_unidade}/{self.unidade_medida}"

class Pizza(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    tipo_pizza = models.ForeignKey(TipoPizzas, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='pizzas/', blank=True, null=True)
    preco_base = models.DecimalField(max_digits=8, decimal_places=2)
    modo_preparo = models.IntegerField()
    tempo_preparo = models.IntegerField()
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    @property
    def preco_total(self):
        total = self.preco_base
        for ingrediente_pizza in self.ingredientepizza_set.all():
            total += ingrediente_pizza.custo_ingrediente
        return total

class IngredientePizza(models.Model):
    # Relaciona o Ingrediente Pizza com a Pizza
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    # Relaciona o Ingrediente Pizza com o Ingrediente
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    # 0.031
    quantidade_numerica = models.DecimalField(max_digits=8, decimal_places=3)
    
    # 300 gramas, 1 colher , 1 fatia
    quantidade_texto = models.CharField(max_length=50, blank=True)


    
    @property
    def custo_ingrediente(self):
        return self.ingrediente.preco_unidade * self.quantidade_numerica

    @property
    def quantidade_display(self):
        if self.quantidade_texto:
            return f"{self.quantidade_numerica} {self.ingrediente.unidade_medida} ({self.quantidade_texto})"
        return f"{self.quantidade_numerica} {self.ingrediente.unidade_medida}"

    
