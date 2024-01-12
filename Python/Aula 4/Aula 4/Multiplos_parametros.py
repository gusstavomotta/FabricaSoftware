"""
Exemplos de funções que recebem múltiplos parametros
Parametros nomeados e posicionais
"""

# Função que recebe diversos parâmetros não nomeados
def calc_custo_projeto(*args):
#    print(args, type(args))
    soma_custo=0
    for val in args:
        soma_custo+=val
    return soma_custo

print('Custo total do projeto 1: ', calc_custo_projeto(10, 34, 20))
print('Custo total do projeto 2: ', calc_custo_projeto(100, 230, 450, 500, 600))

# Função que recebe diversos parâmetros nomeados
def conta_partic_projeto(**kwargs):
#    print(kwargs, type(kwargs))
    cont=0
    for item in kwargs.keys():
        cont+=1
    return cont

print('Número de participantes do projeto 1: ',
      conta_partic_projeto(nome1='Evandro', nome2='Juca Bala', nome3='Jesus'))

# Para contar participantes, exceto coordenador
def conta_particsc_projeto(**kwargs):
    cont=0
    for val in kwargs.values():
        if val!='Coordenador':
            cont+=1
    return cont

print('Número de participantes do projeto 2: ',
      conta_particsc_projeto(funcao1='Auxiliar', funcao2='Analista', funcao3='Coordenador'))
print('Número de participantes do projeto 3: ',
      conta_partic_projeto(funcao1='Auxiliar', funcao2='Analista', funcao3='Coordenador', funcao4='Programador'))

# Combinação de argumentos variávies, posicionais e nomeados
def calc_estat_projeto(*args, **kwargs):
    soma_custo=0
    for val in args:
        soma_custo=+val
        cont=0
    for val in kwargs.values():
        if val!='Coordenador':
            cont+=1
    estat_proj=[soma_custo, cont]
    return estat_proj

dados_proj=calc_estat_projeto(150, 350, 200, 500, funcao1='Analista', funcao2='Programador')
print(dados_proj)
print('Numero de participantes do projeto 1: {}. Soma do custo do projeto 1: {}'
      .format(dados_proj[1], dados_proj[0]))
