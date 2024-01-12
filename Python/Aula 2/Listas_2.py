# Lista podem ter valores de qualquer tipo, tem tamanho variável
# São coleções ordenadas e flexíveis e podem ser aninhadas
# Um recurso que em algumas linguagens exigiria implementação com algum código extra
lista1 = [15, 10, 24, 32]
lista2 =['alto', 100, 'medio', 'baixo']

# lista3 é uma referência para o mesmo objeto referenciado por lista1
lista3 = lista1 # lista3 aponta para a mesma lista
print(lista1, lista2, lista3)
lista1[1] = 25 # altera um elemento da lista1
print(lista1, lista3) # vai alterar a lista3?

# Listas com referências para listas
lista4 = [lista1, lista2]
print(lista4)
lista1=[200, 100, 300, 50]
print(lista4)
print(lista1, lista3)