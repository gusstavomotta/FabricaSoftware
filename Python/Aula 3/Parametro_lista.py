lista1=[10, 20, 30]
def muda_lista(lista_f):
    lista_f[1]=15
    print(lista_f)

muda_lista(lista1)
print(lista1)

lista2=[10, 20, 30]
def nova_lista(lista_f):
    lista_f=[100, 200, 300]
    print(lista_f)

nova_lista(lista2)
print(lista2)