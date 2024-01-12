"""
Pedir ao usuario: Se tem celular e
qual plataforma
"""
num_part = int(input('Qual o número de participantes da pesquisa: '))
cont = 1
cont_and = 0
cont_ios = 0
cont_out = 0
cont_nao = 0
while cont <= num_part:
    temcel = input('Possui celular/smartphone? (S/N): ')
    if temcel == 'S':
        sisop = input('Qual o sistema operacional? (Android/IOS/Outro: ')
        if sisop == 'Android':
            cont_and = cont_and+1
        elif sisop == 'IOS':
            cont_ios = cont_ios+1
        else:
            cont_out = cont_out + 1
    else:
        cont_nao = cont_nao+1
    cont = cont+1
print('Dentre os participantes {} não possuem celular'.format(cont_nao))
print('Dentre os participantes {} possuem sistema Android'.format(cont_and))
print('Dentre os participantes {} possuem sistema IOS'.format(cont_ios))
print('Dentre os participantes {} possuem outro sistema'.format(cont_out))
