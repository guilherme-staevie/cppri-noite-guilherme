from tabnanny import verbose

from django.db import models

import fornecedores.models

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome do produto', unique=True)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, help_text='Preço do produto')
    quantidade = models.DecimalField('Quantidade', max_digits=5, decimal_places=2, help_text='Quantidade do produto')
    fornecedor = models.ForeignKey(fornecedores.models.Fornecedor, verbose_name='Fornecedor', help_text='Nome do fornecedor', on_delete=models.CASCADE, related_name='fornecedor')


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome