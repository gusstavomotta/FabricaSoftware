"""
Exemplos de funções com diferentes definições de parâmetros
"""

def f_calc_desc(valor, percdesc):
    if percdesc>=0:
        desconto=valor*(percdesc/100)
    else:
        desconto=0
    valorcompra=2000
    return desconto

valorcompra=int(input('Informe o valor da compra '))
percdesc=int(input('Informe o percentual de desconto '))

vdesconto=f_calc_desc(valorcompra, percdesc)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))
