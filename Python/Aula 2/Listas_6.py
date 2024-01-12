"""
Incluindo dados em listas
"""

lista_nomes=[]
lista_idades=[]

nome=input('Nome do estudante: ')
while nome !='':
    idade=int(input('Idade do estudante: '))
    lista_nomes.append(nome)
    lista_idades.append(idade)
    nome = input('Nome do estudante: ')

# Mostra os nomes
for nome in lista_nomes:
    print(nome)

# Mostra idades usando posição
cont=0
num_estudantes=len(lista_nomes)
while cont<num_estudantes:
    print(lista_idades[cont])
    cont=cont+1
