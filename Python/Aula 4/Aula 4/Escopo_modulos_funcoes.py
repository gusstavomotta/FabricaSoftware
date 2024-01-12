"""
Exemplo de escopo de objetos no módulo e em funções
"""
nome='Evandro'
idade=50

def idade_10(idade):
# idade é uma variável local, parametro
    idade=idade+10
    return idade

prox_idade=idade_10(idade)
print(prox_idade)
print(idade)

def idade_mais(maisanos):
# idade utilizada de forma global
    idade20=idade+maisanos
    return idade20

prox_idade=idade_mais(20)
print(prox_idade)

def idade_menos(menosanos):
# acesso a variável global idade
# altera o valor da variável
    global idade
    idade=idade-menosanos
    return idade

idade_ant=idade_menos(15)
print(idade_ant)
print(idade)


