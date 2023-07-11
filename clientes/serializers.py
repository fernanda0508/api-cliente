from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    #  a partir do data consigo buscar todos os campos
    # do serializer
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF inválido!"})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua número neste campo!"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O celular deve seguir o padrão: '11 9856-2345' (respeitando os espaços e traço)"})
        return data

        