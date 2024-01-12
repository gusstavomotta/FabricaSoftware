"""
Exemplos de funções com diferentes definições de parâmetros
"""

def f_calc_desc(valor=1000, percdesc=10):
    if percdesc>=0:
        desconto=valor*(percdesc/100)
    else:
        desconto=0
    return desconto

valorcompra=int(input('Informe o valor da compra '))
percdesc=int(input('Informe o percentual de desconto '))

vdesconto=f_calc_desc(valorcompra, percdesc)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))

vdesconto=f_calc_desc(percdesc=percdesc, valor=valorcompra)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))

vdesconto=f_calc_desc()
print('Valor: {}. Desconto: {}'.format(1000, vdesconto))

vdesconto=f_calc_desc(percdesc=percdesc)
print('Valor: {}. Desconto: {}'.format(1000, vdesconto))

vdesconto=f_calc_desc(valor=valorcompra)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))
