from carro import *

def menu():

    op = 1

    while op != 0:

        print("\n1- Inserir veículo no sistema.")
        print("2- Remover veículo do sistema.")
        print("3- Alterar atributo do veículo.")
        print("4- Aumentar preço dos automóveis.")
        print("5- Diminuir preço dos automóveis.")
        print("6- Mostrar todos os veículos no sistema.")
        print("7- Mostrar veículo mais caro.")
        print("0- Encerrar Programa. ")

        op = int(input("\nQual operação deseja realizar? "))
        if op == 1:
            adicionar_veiculo(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 2:
            remover_veiculo(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 3:
            alterar_atributo_veiculo(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 4:
            aumentar_preco(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 5:
            diminuir_preco(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 6:
            mostrar_veiculos(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 7:
            calcular_maior_preco(lista_carros)
            input("\nPressione ENTER para continuar!")

        elif op == 0:
            op = 0

        else:
            print("Operação inválida: ")


menu()
