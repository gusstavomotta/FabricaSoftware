from funcoes import *
from crud import *
from classes import *

'''ARQUIVO DEDICADO AO MENU'''


def menu():
    '''REALIZA A CHAMADA DE TODAS AS FUNÇÕES'''

    while True:

        '''a cada loop o programa irá carregar as agendas do csv, atualiza-las e escreve-las ordenadas'''
        lst_de_agendas = carregar_agendas()
        lst_de_agendas = quick_sort_agendas(lst_de_agendas)
        escrever_agendas_csv(lst_de_agendas)
        '''a cada loop o programa irá carregar os usuarios do csv e escreve-los'''
        lst_de_usuarios = carregar_usuarios()
        escrever_usuario(lst_de_usuarios)

        '''Printa o menu, faz o scan da opção e chama as funções'''
        print("1- Adicionar agenda.")
        print('2- Adicionar usuário.')
        print('3- Excluir agenda.')
        print('4- Alterar agenda.')
        print('5- Printar todas agendas.')
        print("6- Buscar agendas por tipo.")
        print("7- Buscar agendas por usuário.")
        print("8- Buscar agendas por período.")
        print("9- Buscar agendas por recurso.")
        print("0- Encerrar programa.")

        op = int(input("Qual operação deseja realizar? "))

        if op == 1:
            adicionar_agenda(lst_de_agendas, lst_de_usuarios)
            input("Pressione ENTER para continuar! ")
        elif op == 2:
            adicionar_usuario(lst_de_usuarios)
            input("Pressione ENTER para continuar! ")
        elif op == 3:
            excluir_agenda(lst_de_agendas, lst_de_usuarios)
            input("Pressione ENTER para continuar! ")
        elif op == 4:
            alterar_agenda(lst_de_agendas, lst_de_usuarios)
            input("Pressione ENTER para continuar! ")
        elif op == 5:
            printar_lst_agendas(lst_de_agendas)
            input("Pressione ENTER para continuar! ")
        elif op == 6:
            buscar_agendas_por_tipo(lst_de_agendas)
            input("Pressione ENTER para continuar! ")
        elif op == 7:
            exibir_agendas_do_usuario(lst_de_agendas, lst_de_usuarios)
            input("Pressione ENTER para continuar! ")
        elif op == 8:
            buscar_agendas_por_periodo(lst_de_agendas)
            input("Pressione ENTER para continuar! ")
        elif op == 9:
            buscar_agendas_por_recurso(lst_de_agendas)
            input("Pressione ENTER para continuar! ")
        elif op == 0:
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()
