"""
- Conjuntos são dicionários sem valores, somente com chaves
- Considerada uma coleção não ordenada de valores únicos
"""
# Criação de dois conjuntos
conj1 = {1, 3, 5}
conj2 = {3, 7, 9}
# Lista com valores duplicados
lista_dup = [1, 1, 3,  5, 5, 5, 4, 7, 9]
print(lista_dup)

# A atribuição de uma lista para um conjunto elimina as duplicações
conj3 = set(lista_dup)
print(conj1, conj2, conj3)

# Não é possível acessar por deslocamento
#print(conj1[1])

# Mas é possível iterar
print('Iterando sobre o conjunto')
for c1 in conj1:
    print(c1)

# Existem várias operações em conjuntos
# Operações tradicionais da teoria matemática dos conjuntos
print(conj1.union(conj2))
print(conj1.intersection(conj2))
print(conj1.difference(conj2))

# Adicionar valores em conjuntos
conj1.add(9)
conj1.add(5)
print(conj1, conj2)