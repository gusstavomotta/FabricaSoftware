from Metodos_classes import *


def menu():

    op = 0
    while op != 7:

        print("\n~~~~~~~~ MENU ~~~~~~~~")
        print("1- Carregar dados.")
        print("2- Ordenar por data.")
        print("3- Ordenar por nome.")
        print("4- Calcula soma, média e a contagem de atendimentos.")
        print("5- Printar listas.")
        print("6- Realizar Busca.")
        print("7- Encerrar programa.")
        op = int(input("\nInsira a operação que você deseja realizar: "))

        if op == 1:
            listaPets = carregar_dados_pets()
            listaAtendimentos = carregar_dados_atendimentos()
            input("\nPression ENTER para continuar!")

        elif op == 2:
            ordenada_por_data = quick_sort(listaAtendimentos)
            for i in ordenada_por_data:
                print(i)

            input("\nPression ENTER para continuar!")

        elif op == 3:
            ordenada_por_nome = ordenar_lista_nome(listaPets)
            for i in ordenada_por_nome:
                print(i)
            input("\nPression ENTER para continuar!")

        elif op == 4:
            calcular_soma_media_por_pet(listaAtendimentos)
            input("\nPression ENTER para continuar!")

        elif op == 5:
            printar_lista(listaPets)
            printar_lista(listaAtendimentos)
            input("\nPression ENTER para continuar!")

        elif op == 6:
            posicao = realizar_busca(listaPets)
            print(posicao)
            input("\nPression ENTER para continuar!")


        else:
            return


menu()
