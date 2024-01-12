"""
Exemplos mostrados no livro:
A Beginners Guide to Python 3 Programming
"""
# Inteiros
"""
x = 1
print(x)
print(type(x))
x = 100000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))

# float
exchange_rate = 1.83
print(exchange_rate)
print(type(exchange_rate))

# Complex numbers
c1 = 1j
c2 = 2j
print('c1:', c1, ', c2:', c2)
print(type(c1))
print(c1.real)
print(c1.imag)

# Boolean
all_ok = True
print(all_ok)
all_ok = False
print(all_ok)
print(type(all_ok))
# 0 e 1 podem ser considerados booleanos
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))
"""
# Operações com números
home = 10
away = 15
print(home + away)
print(type(home + away))
print(10 * 4)
print(type(10*4))
goals_for = 10
goals_against = 7
print(goals_for - goals_against)
print(type(goals_for - goals_against))

#divisao=100/20
divisao=100//20
print(divisao)
print(type(divisao))

print('Modulus division 4 % 2:', 4 % 2)
print('Modulus division 3 % 2:', 3 % 2)

# Resultado pode ser inesperado
i = 3 * 0.1
print(i)
print(type(i))

# Operadores de atribuição
x = 0
x += 1
print(x)
x *=2
print(x)
x **=2
print(x)
