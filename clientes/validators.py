import re
from validate_docbr import CPF


def validar_cpf(numero_de_cpf):
    cpf = CPF()
    return cpf.validate(numero_de_cpf)


def validar_nome(nome):
    return nome.isalpha()


def validar_rg(rg):
    return len(rg) == 9


def validar_celular(celular):
    """
    Verifica se o celular é válido
    """
    modelo = '[0-9{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)

    return resposta
