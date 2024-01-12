
def f_calc_desc(valor, percdesc=10):
    if percdesc>=0:
        desconto=valor*(percdesc/100)
    else:
        desconto=0
    valor=100
    return desconto

valorcompra=int(input('Informe o valor da compra '))
percdesc=int(input('Informe o percentual de desconto '))

vdesconto=f_calc_desc(valorcompra, percdesc)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))

#vdesconto=f_calc_desc()
#print('Valor: {}. Desconto: {}'.format(1000, vdesconto))

#vdesconto=f_calc_desc(percdesc=percdesc)
#print('Valor: {}. Desconto: {}'.format(1000, vdesconto))

vdesconto=f_calc_desc(valor=valorcompra)
print('Valor: {}. Desconto: {}'.format(valorcompra, vdesconto))