
consumo = []
producao = []


def leitura(lstconsumo, lstproducao):
    for dia in range(0, 4):
        producaodia = int(
            input('Informe a produção do dia ' + str(dia + 1) + ' '))
        consumodia = int(input('Informe o consumo do dia '+str(dia+1)+' '))
        lstconsumo.append(consumodia)
        lstproducao.append(producaodia)


def consperiodo(lstconsumo, lstproducao, diaini, diafim):
    cont = diaini-1
    while cont <= diafim-1:
        print('Produção no dia {}: {}'.format(cont+1, lstproducao[cont]))
        print('Consumo no dia {}: {}'.format(cont | +1, lstconsumo[cont]))
        saldo = lstproducao[cont]-lstconsumo[cont]
        print('Saldo no dia {}: {}'.format(cont+1, saldo))
        cont = cont+1


def maiorproducao(lstproducao):
    maiorprod = lstproducao[0]
    diamaior = 0
    for dia in range(1, 4):
        if lstproducao[dia] > maiorprod:
            maiorprod = lstproducao[dia]
            diamaior = dia
    return [maiorprod, diamaior]


def saldo_mes(lstproducao, lstconsumo):
    total_cons = 0
    total_prod = 0
    for dia in range(0, 4):
        total_cons = total_cons+lstconsumo[dia]
        total_prod = total_prod+lstproducao[dia]
    return [total_prod, total_cons]


leitura(consumo, producao)
opcao = 0
while opcao != 4:
    print('1-Consulta dados de um período')
    print('2-Consulta maior produção')
    print('3-Consulta saldo mês')
    print('4-Sair')
    opcao = int(input('Informe a opção: '))
    if opcao == 1:
        diaini = int(input('Informe o dia inicial: '))
        diafim = int(input('Informe o dia final: '))
        consperiodo(consumo, producao, diaini, diafim)
    else:
        if opcao == 2:
            dados = maiorproducao(producao)
            print('Maior produção foi: {} e ocorreu no dia: {}'.format(
                dados[0], dados[1]+1))
        else:
            if opcao == 3:
                dados = saldo_mes(producao, consumo)
                print('Total produzido no mês: ',  dados[0])
                print('Total consumido no mês: ', dados[1])
                print('Saldo no mês: ', dados[0]-dados[1])
