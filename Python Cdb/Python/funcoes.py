'''ARQUIVO PARA ARMAZENAR AS FUNÇÕES DO PROGRAMA'''
import datetime


def quick_sort_agendas(lst_agendas):
    
    '''QUICK SORT PARA REALIZAR A ORDENAÇÃO DA LISTA DE AGENDAS'''
    if len(lst_agendas) > 1:
        pivo = len(lst_agendas) // 2
        valor = lst_agendas[pivo].data, lst_agendas[pivo].hora

        esquerda = [agenda for agenda in lst_agendas if (agenda.data, agenda.hora) < valor]
        meio = [agenda for agenda in lst_agendas if (agenda.data, agenda.hora) == valor]
        direita = [agenda for agenda in lst_agendas if (agenda.data, agenda.hora) > valor]

        return quick_sort_agendas(esquerda) + meio + quick_sort_agendas(direita)
    else:
        return lst_agendas


def printar_lst_agendas(lst_agendas):
    '''PRINTA TODAS AS AGENDAS NA LISTA'''
    '''verifica se a lista está vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    '''faz uma repetição e printa'''
    for agenda in lst_agendas:
        print(f"\nData: {agenda.data}\nHora: {agenda.hora}\nTipo: {agenda.tipo}\nDescrição: {agenda.descricao}\nParticipantes: {agenda.participantes}\nRecursos: {agenda.recursos}\n")


def printar_agenda(agenda):
    '''realiza o print de uma unica agenda'''
    print(f"Data: {agenda.data}, Hora: {agenda.hora}, Tipo: {agenda.tipo}, Descrição: {agenda.descricao}, Participantes: {agenda.participantes}, Recursos: {agenda.recursos}\n")


def buscar_agendas_por_tipo(lst_agendas):
    '''BUSCA COMPROMISSOS COM BASE NO TIPO INSERIDO PELO USUÁRIO'''
    
    '''verifica se a lista está vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    
    '''lista os tipos possiveis de agenda'''
    tipos_agendas = ['compromisso', 'lembrete']
    tipo = str(input("Insira o tipo da agenda (Compromisso/Lembrete): "))
    '''verifica se o inserido é valido'''
    while True:
        if tipo not in tipos_agendas:
            print("Tipo inválido, insira novamente!")
            continue
        break

    '''faz a listagem conforme o tipo inserido e printa'''
    lst_por_tipo = [agenda for agenda in lst_agendas if agenda.tipo == tipo]
    if len(lst_por_tipo) == 0:
        print("Não foram encontradas agendas com o tipo especificado.")
    else:
        print("Agendas encontradas:")
        printar_lst_agendas(lst_por_tipo)


def buscar_agendas_por_periodo(lst_agendas):
    '''BUSCA COMPROMISSOS DENTRO DE UM DETERMINADO PERÍODO'''
    
    '''verifica se a lista esta vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    
    '''pede ao usuario informar data de inicio e de fim da consulta'''
    data_inicio = input("Insira a data de início do período (DD/MM/AAAA): ")
    data_fim = input("Insira a data de fim do período (DD/MM/AAAA): ")
    '''valida as datas e as transforma para o formato dd/mm/aaaa'''
    try:
        data_inicio = datetime.datetime.strptime(data_inicio, "%d/%m/%Y").strftime("%d/%m/%Y")
        data_fim = datetime.datetime.strptime(data_fim, "%d/%m/%Y").strftime("%d/%m/%Y")
    except ValueError:
        print("Data inválida, Insira novamente!")
        return
    
    '''armazena todas as agendas que estão dentro do período especificado e realiza o print'''
    agendas_periodo = [agenda for agenda in lst_agendas if data_inicio <= agenda.data <= data_fim]
    if len(agendas_periodo) == 0:
        print("Não foram encontradas agendas no período especificado.")
    else:
        print("Agendas encontradas:")
        printar_lst_agendas(agendas_periodo)


def buscar_agendas_por_recurso(lst_agendas):
    '''BUSCA COMPROMISSOS COM BASE NO RECURSO INSERIDO PELO USUÁRIO'''

    '''verifica se a lista está vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    
    '''faz o scan do recurso que o usuário informar'''
    recurso = str(input("Insira o recurso desejado: "))
    '''armazena todas as agendas com o mesmo recurso e realiza o print'''
    lst_por_recurso = [agenda for agenda in lst_agendas if recurso in agenda.recursos]

    if len(lst_por_recurso) == 0:
        print("Não foram encontradas agendas com o recurso especificado.")
    else:
        print("Agendas encontradas:")
        printar_lst_agendas(lst_por_recurso)


def exibir_agendas_do_usuario(lst_agendas, lst_usuarios):
    '''EXIBE OS COMPROMISSOS DE UM USUÁRIO ESPECÍFICO'''
    
    '''realiza a validação do usuário'''
    usuario_encontrado = None
    while True:
        '''faz o scan do nome, depois realiza uma for/loop para verificar se o nome existe no csv de usuarios
        caso existir ele retorna o usuario'''
        nome_usuario = str(input("Insira o nome do usuário: "))
        usuario_encontrado = next((usuario for usuario in lst_usuarios if usuario.nome == nome_usuario),None)
        if usuario_encontrado:
            break
        else:
            print("Usuário não encontrado")
    '''realiza um loop para adicionar em uma lista todos as agendas do usuário informado e printa'''
    agendas_do_usuario = [agenda for agenda in lst_agendas if str(usuario_encontrado.chatId) in agenda.participantes]

    if len(agendas_do_usuario) == 0:
        print("Não foram encontrados compromissos para o usuário especificado.")
    else:
        print(f"Agendas do usuário {nome_usuario}:")
        printar_lst_agendas(agendas_do_usuario)


def verifica_lst_vazia(lst):
    '''verifica se alguma lista passada por referencia está vazia'''
    if not lst:
        print("Lista vazia!")
        return False
  
    
def validar_usuario(participantes, lst_usuarios):
    '''Verifica se os participantes correspondem a algum usuário na lista de usuários'''
    chat_ids = []
    '''realiza a repetição'''
    for participante in participantes:
        for usuario in lst_usuarios:
            '''caso o nome inserido bater com o nome armazenado o chatId é retornado para a lista de ids'''
            if usuario.nome == participante:
                chat_ids.append(usuario.chatId)
                break
        else:
            return None
    return chat_ids
