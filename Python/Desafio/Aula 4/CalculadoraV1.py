# Desafio calculadora 1.0
# Gustavo Oliveira da Motta
# Última modificação 26/03/2023

# funções anônimas criadas, retornam as operações 
def retornaSoma():
    #retorna soma 
    return lambda x, y: x + y


def retornaSubtracao():
    #retorna subtração 
    return lambda x, y: x - y


def retornaMultiplicacao():
    #retorna o produto
    return lambda x, y: x * y


def retornadivisao():
    #retorna o resto 
    return lambda x, y: x / y


def retornaPotencia():
    #retorna a potencia
    return lambda x, y: pow(x, y)

# realiza a entrada de dados, a operação desejada e os valores

def entradaDados():

    print("\nInforme dois valores:")
    x = int(input("x: "))
    y = int(input("y:: "))
    print("\nInforme qual operação matemática você quer realizar.")
    print(" + Para adição.")
    print(" - Para subtração.")
    print(" * Para multiplicação.")
    print(" / Para divisão.")
    print(" ^ Para potenciação.")
    op = input("\nOperação:")
    #retorna os valores inseridos
    return op, x, y

# valida a operação e realiza os calculos

def calculadora():

    while True:

        op, x, y = entradaDados()

        if op == '+':
            # armazena a função em uma variável
            resultado = retornaSoma()
            # passa os numeros digitados como argumento para a função e realiza o calculo
            print("O resultado é: ", resultado(x, y))
            return False

        elif op == '-':
            # armazena a função em uma variável
            resultado = retornaSubtracao()
            # passa os numeros digitados como argumento para a função e realiza o calculo
            print("O resultado é: ", resultado(x, y))
            return False

        elif op == '*':
            # armazena a função em uma variável
            resultado = retornaMultiplicacao()
            # passa os numeros digitados como argumento para a função e realiza o calculo
            print("O resultado é: ", resultado(x, y))
            return False

        elif op == '/':
            # armazena a função em uma variável
            resultado = retornadivisao()
            # passa os numeros digitados como argumento para a função e realiza o calculo
            print("O resultado é: ", resultado(x, y))
            return False

        elif op == '^':
            # armazena a função em uma variável
            resultado = retornaPotencia()
            # passa os numeros digitados como argumento para a função e realiza o calculo
            print("O resultado é: ", resultado(x, y))
            return False

        else:
            print("Opção inválida!")


calculadora()
