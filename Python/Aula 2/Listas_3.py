"""
A classe lista apresenta diversos métodos
Os métodos permitem ordenar, inserir, remover valores, etc
"""
lista1=[35, 43, 12, 67, 88, 90]
lista2=[2,4,6,8,10]

# Métodos para manipular listas
lista1.sort(reverse=True)
print('Lista 1 ordenada: ', lista1)

# Remove um valor da lista, de determinada posição
print(lista2.pop(1))
print('Lista 2 após remover 1:', lista2)

# Inserção em determinada posiçao
lista1.insert(2, 450)
print('Lista 1 após inserir 450: ', lista1)

# Adição de listas
lista1_mais_2 = lista1 + lista2
print('Lista1_2: ',lista1_mais_2)