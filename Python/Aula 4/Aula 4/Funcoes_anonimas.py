"""
Funções anônimas são criadas usando a expressão lambda
É possível criar em diferentes contextos
Lambda retorna uma referência para uma função
"""
func=lambda x: x*10
print(func(10))
func1 = lambda x: x * x
print(func1(20))

def retornaf(x):
    if x=='A':
       return lambda y, z: z>y
    else:
        return lambda y,z: z<y

func2=retornaf('A')
print(func2(10,20))

func3=retornaf('B')
print(func3(10,20))

lista1=[10, 20, 30]
lista2=list(map(lambda x: x**2, lista1))
print(lista2)
print((lambda v1: v1**3)(3))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, lista)))

