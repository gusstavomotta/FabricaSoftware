"""
Cria uma função que retorna uma referência para um objeto do tipo função
Neste caso a função f_calc decide como calcular e retorna a função que irá fazer o cálculo
"""
def f_calc(opcao):
    def f10(num):
        return num*0.10

    def f20(num):
        return num*0.20
    if opcao==1:
        return f10
    else:
        return f20

f=f_calc(1)
print(f(20))

# Tipo do objeto função
print(type(f_calc))
# Posição de memória da função
print(f_calc)