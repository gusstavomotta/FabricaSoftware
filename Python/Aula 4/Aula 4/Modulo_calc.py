z=100
lista=[10, 20, 30]
def f_calc_soma(x, y):
    return x+y

def f_calc_mult(x, y):
    return x*y

def f_calc_potencia(x,y):
    return x**y

def f_soma_lista(lista):
    soma=0
    for l in lista:
        soma=soma+l
    return soma

def f_soma_valores(*args):
    soma=0
    for v in args:
        soma=soma+v
    return soma


