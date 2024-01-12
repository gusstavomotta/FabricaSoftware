"""
Função eval é usada para executar uma operação armazenada em uma string
É util para personalizar a execução de determinadas rotinas
"""
soma="2+3"
print(eval(soma))

def f_soma(x, y):
    return x+y

operacao='f_soma(10,20)'
print(eval(operacao))