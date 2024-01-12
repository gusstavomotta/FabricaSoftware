
def leitura_dados():
    operador1=int(input('Informe o primeiro operador '))
    operador2 = int(input('Informe o segundo operador '))
    operacao=input('Informe a operacao (/-+*)')
    return [operador1, operador2, operacao]

def calcula(dados):
    operador1=dados[0]
    operador2=dados[1]
    operacao=dados[2]
    if dados[2]=='+':
        funcao=lambda operador1, operador2:operador1+operador2
    elif dados[2]=='-':
        funcao = lambda operador1, operador2:operador1-operador2
    elif dados[2]=='/':
        funcao = lambda operador1, operador2:operador1/operador2
    else:
        funcao = lambda operador1, operador2:operador1*operador2
    return funcao(operador1,operador2)

def leitura_dados_mais():
    operador1=int(input('Informe o primeiro operador '))
    operador2 = int(input('Informe o segundo operador '))
    operador3=int(input('Informe o terceiro operador '))
    operador4=int(input('Informe o quarto operador '))
    operacao=input('Informe a operacao (/-+*)')
    return [operador1, operador2, operador3, operador4, operacao]

def calcula_mais(operacao='+'):
    def calcula_soma(*args):
        res=0
        for v in args:
            res=res+v
        return res

    def calcula_sub(*args):
        res=args[0]
        for k, v in enumerate(args):
            if k>0:
                res=res-v
        return res

    def calcula_div(*args):
        res=args[0]
        for k, v in enumerate(args):
            if k>0:
                res=res/v
        return res

    def calcula_mult(*args):
        res = 1
        for v in args:
            res = res * v
        return res

    if operacao=='+':
        return calcula_soma
    elif operacao=='-':
        return calcula_sub
    elif operacao=='/':
        return calcula_div
    else:
        return calcula_mult