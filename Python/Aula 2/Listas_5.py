"""
Fatiamento de listas, acesso por deslocamento
List compreensions
"""

# Fatiamento, com indicação de salto
lista_num=list(range(10))
print(lista_num)
print(lista_num[::2])
print(lista_num[::-2])
print(lista_num[2:8:3])

# List comprehensions
# Expressões que criam listas
pares = [num for num in lista_num if num%2==0]
print('Numeros pares ', pares)

# A partir da lista completa dos anos de 900 a 2022 gera lista com bissextos
anosbissextos=[ano for ano in range(1900, 2022)
               if(ano%4==0 and ano%100!=0) or (ano%400==0)]
print('Anos bissextos ', anosbissextos)
print('Último ano bissexto: ',anosbissextos[-1])

# Desempacotar listas
# Operador * obtém todos os elementos, menos o primeiro
first, *rest=anosbissextos
print(first)
print(rest)

# Aninhamento de listas em list comprehension
# Faz um produto cartesiano dos valores das listas
print('Listas l1 e l2: ', l1, l2)
l5 = [v1*v2 for v1 in l1 for v2 in l2]
print(l5)