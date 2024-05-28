from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validar_cpf(data['cpf']):
            raise serializers.ValidationError({"cpf": "Número de CPF inválido"})

        if not validar_nome(data['nome']):
            raise serializers.ValidationError({"nome": "Não inclua números neste campo"})

        if not validar_rg(data['rg']):
            raise serializers.ValidationError({"rg": "O RG deve ter 9 dígitos"})

        if not validar_celular(data['celular']):
            raise serializers.ValidationError({"celular": "O número do celular precisa seguir esse padrão: 11 91234-1234"})

        return data
