"""
Exemplo de função de alta ordem apply
"""



# Função apply criada é de alta ordem
def apply(function, x):
    result = function(x)
    return result

# Função que será aplicada por apply
def f_soma(x):
    return x[0] + x[1]

# Aplicação da função
res = apply(f_soma, (10, 20))
print(res)

# Apply com mútiplos argumentos
def apply1(function, *args):
    result = function(*args)
    return result

# Função que será aplicada por apply
def f_soma(*args):
    soma=0
    for v in args:
        soma = soma+v
    return soma

# Aplicação da função
res = apply1(f_soma, 10, 20, 30)
print(res)
