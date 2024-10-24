from django import forms

from .models import Fornecedor


class FornecedorModelForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do fornecedor é um campo obrigatório'},
            'cnpj': {'required': 'O Cnpj do fornecedor é um campo obrigatório','unique':'CNPJ já cadastrado'},
            'fone': {'required': 'O numero do telefone é um campo obrigatorio'},
        }