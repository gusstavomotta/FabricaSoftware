# declaração das listas dos meses com 30 e 31 dias
meses31 = ['Janeiro', 'Março', 'Maio',
           'Julho', 'Agosto', 'Outubro', 'Dezembro']
meses30 = ['Abril', 'Junho', 'Setembro', 'Novembro']
# declaração das listas para armazenar o consumo e a produção de energia/ valores inseridos pelo usuario
listaProducao = []
listaConsumo = []

# função para definir o mes


def mes():
    # faz o scan do mes que p usuario informar e retorna o valor 30/31 ou 28 para a variavel dias referente a quantos dias tem o mes informado
    while True:
        dias = input("Qual mês do ano você gostaria de informar ao programa? ")
        if dias in meses31:
            return 31
        elif dias in meses30:
            return 30
        elif dias == 'Fevereiro':
            return 28
        else:
            print("Mês inválido, tente novamente.")

# entrada de dados


def entradaDados(dias):

    # executa um loop que a condiçaõ de parada é o numero de dias do mes, definido na função "mes()""
    for i in range(dias):
        producao = float(
            input(f"\nQuantos KW foram produzidos no dia {i + 1 }? "))
        listaProducao.append(producao)
        consumo = float(input("Quantos KW foram consumidos nesse dia?"))
        listaConsumo.append(consumo)

# funçaõ para mostrar informações em determinado período


def mostraPeriodo(dias, listaConsumo, listaProducao):

    # início do loop
    while True:
        # valida se a lista está ou não vazia
        if not listaConsumo or not listaProducao:
            print("Impossível verificar, nenhum dado foi inserido ainda.")
            # retorna false e para o loop (condição de parada)
            return False
        else:
            inicio = int(
                input("Insira dia de início do período a ser consultado: "))
            fim = int(input("Insira o dia final do período a ser consultado: "))
            if fim > dias:
                print(
                    f"Você nao pode consultar mais do que os {dias} dias do mês! ")

            else:
                consumo = sum(listaConsumo[inicio - 1:fim])
                producao = sum(listaProducao[inicio - 1: fim])
                print(
                    f"\nA produção total no período consultado ficou em: {consumo} KW.")
                print(
                    f"O consumo total no período consultado ficou em: {producao} KW.")
                print(f"Diferenca: {consumo - producao} KW.")
                # realiza todos as entradas, calculos e depois printa todas as informações / condição de parada
                return False

# função que mostra o dia que teve a maior produção


def producaoMaxima(dias):
    # inicio do loop
    while True:
        # veririca se a lista etá vazia
        if not listaConsumo or not listaProducao:
            print("Impossível verificar, nenhum dado foi inserido ainda.")
            # condição de parada
            return False
        else:
            maximo = max(listaProducao)
            diaMax = listaProducao.index(maximo)
            print(
                f"A produção máxima foi de {maximo}KW no dia {diaMax + 1}.\n")
            # retira o maior valor da lista e sua posição, printa os mesmos e incrementa 1 na posição para printar o dia correto// condição de parada
            return False

# printa as informações gerais


def infoGeral():
    # inicio do loop
    while True:
        # verifica se a lista esta vazia
        if not listaConsumo or not listaProducao:
            print("Impossível verificar, nenhum dado foi inserido ainda.")
            # condição de parada
            return False
        else:
            consumoTotal = sum(listaConsumo)
            producaoTotal = sum(listaProducao)

            print(f"A produção geral ficou em: {producaoTotal} KW. ")
            print(f"O consumo geral ficou em: {consumoTotal} KW.")
            print(f"Saldo geral: {producaoTotal - consumoTotal} KW.")
            # soma todos os valores das listas, armazena em uma variável e printa na tela as informações// condição de parada
            return False

# print apenas para visualizar as operações disponíveis


def operacoes():

    print("\n[1] Informar a produção e consumo diário.")
    print("[2] Informaçoes gerais do mês.")
    print("[3] Consultar balanço em um período determinado.")
    print("[4] Consultar dia de maior produção.")
    print("[5] Sair.\n")


# declaraão de varáveis
dias = mes()
op = 0
# início do loop
while op != 5:

    # chama a funnção operações
    operacoes()
    # faz o scan da operação que o usuario deseja realizar
    # a partir daqui uma espécie de switch com o input sendo utilizado para realizar uma parada de tela
    op = int(input("Digite o número da opção desejada: \n"))
    if op == 1:
        entradaDados(dias)
        input("Pressione Enter para continuar.")
    elif op == 2:
        infoGeral()
        input("Pressione Enter para continuar.")
    elif op == 3:
        mostraPeriodo(dias, listaConsumo, listaProducao)
        input("Pressione Enter para continuar.")
    elif op == 4:
        producaoMaxima(dias)
        input("Pressione Enter para continuar.")
    elif op == 5:
        print("Encerrando programa...")
        op = 5
    else:
        print("Opção inválida. Tente novamente.")

# fim do programa
