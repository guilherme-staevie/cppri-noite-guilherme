from django import forms

from .models import Produto


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do produto é um campo obrigatório', 'unique':'Produto já cadastrado'},
            'preco': {'required': 'O Cnpj do fornecedor é um campo obrigatório','unique':'CNPJ já cadastrado'},
            'quantidade': {'required': 'A quantidade em estoque do produto é um campo obrigatorio'},
        }