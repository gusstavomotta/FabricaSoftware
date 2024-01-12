# IMPORTA DO PROGRAMA
from sistemaSegurança import *

# LOOP WHILE PARA ESCANEAR A OPERAÇÃO QUE O USUÁRIO QUER REALIZAR E CHAMA AS RESPECTIVAS FUNÇÕES
op = 1
while op != 10:

    print("\n1- Cadastrar funcionário. ")
    print("2- Registrar Ocorrência. ")
    print("3- Consultar occorências pendentes. ")
    print("4- Resolver ocorrência. ")
    print("5- Ignorar ocorrência. ")
    print("6- Listar ocorrências pendentes. ")
    print("7- Listar ocorrências resolvidas.")
    print("8- Listar ocorrências ignoradas.")
    print("9- Ver estatísticas.")
    print("10- Encerrar Programa.")

    op = int(input("\nQual operação deseja realizar? "))

    if op == 1:

        cadastro_funcionarios()
        input("\nPressione ENTER para continuar! ")

    elif op == 2:

        nova_ocorrencia = recebe_ocorrencia()
        pendentes.append(nova_ocorrencia)
        input("\nPressione ENTER para continuar! ")

    elif op == 3:

        consulta_ocorrencia(pendentes)
        input("\nPressione ENTER para continuar! ")

    elif op == 4:

        resolve_ocorrencia(pendentes)
        input("\nPressione ENTER para continuar! ")

    elif op == 5:

        ignora_ocorrencia(pendentes)
        input("\nPressione ENTER para continuar! ")

    elif op == 6:

        if not pendentes:
            print("A lista de ocorrências pendentes está vazia!")

        for i in pendentes:
            print(i)
        input("\nPressione ENTER para continuar! ")

    elif op == 7:

        if not resolvidas:
            print("A lista de ocorrências resolvidas está vazia!")

        for i in resolvidas:
            print(i)
        input("\nPressione ENTER para continuar! ")

    elif op == 8:

        if not ingnoradas:
            print("A lista de ocorrências ignoradas está vazia!")

        for i in ingnoradas:
            print(i)
        input("\nPressione ENTER para continuar! ")

    elif op == 9:

        conta_ocorrencia(pendentes, resolvidas, ingnoradas, dic_funcionarios)
        input("\nPressione ENTER para continuar! ")

    # PARA O PROGRAMA
    elif op == 10:
        op = 10

    else:
        print("Operação inválida!")
        input("\nPressione ENTER para continuar! ")


