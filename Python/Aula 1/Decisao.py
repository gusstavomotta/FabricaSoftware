"""
Exemplos mostrados no livro:
A Beginners Guide to Python 3 Programming
"""

num = int(input('Informe o número: '))
if num > 0:
    print(num, 'é positivo')
    print(num, 'quadrado: ', num * num)
print('Valor: ', num)

# Condição em expressão
pos_neg = 'Positivo' if num>=0 else 'Negativo'
print(pos_neg)

# Implementação com diversos fluxos diferentes
savings = float(input("Informe o valor aplicado: "))
if savings == 0:
    print("Você não possui valores")
elif savings < 500:
    print('Já é um começo')
elif savings < 1000:
    print('Ainda é um valor baixo')
elif savings < 10000:
    print('Está quase')
else:
    print('Parabéns!')

# Com instruções aninhadas
savings = float(input("Informe o valor aplicado: "))
if savings == 0:
    print("Você não possui valores")
else:
    if savings < 500:
        print('Já é um começo')
    else:
        if savings < 1000:
            print('Ainda é um valor baixo')
        else:
            if savings < 10000:
                print('Está quase')
            else:
                print('Parabéns!')