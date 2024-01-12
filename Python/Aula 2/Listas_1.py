"""
- Exemplos de operações com listas
"""

# Criação de listas
l1 = [10, 20, 30]
l2 = [1.2, 2.4, 5.5]
l3 = [] # Lista vazia
l4 = list(('a', 1, 'b', 'c'))

print(l1, l2, l3, l4)

# Laço que obtém cada valor da lista
# Listas são estruturas que permitem iteração
print('Valores de l1')
for v1 in l1:
  print(v1)

# Multiplicação de listas. Tipos diferentes?
#l3 = l1*l2
#print('Multiplicação de l1 por l2: ', l5)

# É possível combinar valores de duas listas
# Aí é possível multiplicar e criar nova lista
for vl1, vl2 in zip(l1, l2):
  v_calc = vl1*vl2
  l3.append(v_calc)

print(l3)

