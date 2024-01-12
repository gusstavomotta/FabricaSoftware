'''ARQUIVO DEDICADO PARA ADICIONAR, EXCLUIR, ALTERAR, CARREGAR ARQUIVOS E ESCREVER NO CSV'''
from classes import *
from funcoes import *
import pandas as pd
import csv
import datetime

def carregar_agendas():
    '''UTILIZA PANDAS PARA CARREGAR OS DADOS DO CSV, 
    PERCORRE AS LINHAS DO CSV, CRIA O OBJETO AGENDA, ADD NA LISTA, 
    RETORNA A LISTA COM OS VALORES'''
    dados_agendas = pd.read_csv('agendas.csv', sep=',', encoding='utf-8')
    info_agendas = dados_agendas.to_dict('records')
    lst_de_agendas = []
    '''realiza uma repetição para criar o objeto e add na lista'''
    for i in info_agendas:
        agenda = Agenda(i['data'], i['hora'], i['tipo'],i['descricao'], i['participantes'], i['recursos'])
        lst_de_agendas.append(agenda)

    return lst_de_agendas


def carregar_usuarios():
    '''UTILIZA PANDAS PARA CARREGAR OS DADOS DO CSV,
    PERCORRE AS LINHAS DO CSV, CRIA O OBJETO USUARIO E ADD NA LISTA,
    RETORNA A LISTA COM OS VALORES'''
    dados_usuarios = pd.read_csv('usuarios.csv')
    info_usuarios = dados_usuarios.to_dict('records')
    lst_de_usuarios = []
    '''realiza a repetição para criar o objeto de add na lista'''
    for i in info_usuarios:
        usuario = Usuario(i['nome'], i['chatId'], i['intervalo_tempo'])
        lst_de_usuarios.append(usuario)
    
    return lst_de_usuarios


def escrever_agendas_csv(lst_agendas):
    '''DEFINE UM CABEÇALHO PADRÃO PARA NAO CAUSAR ERROS NO CARREGAR_AGENDAS, 
    TODA QUE VEZ QUE É CHAMADA ESSA FUNÇÃO REESCREVE O CABEÇALHO, CASO NAO TER CABEÇALHO ELA ADD, 
    RECEBE A LISTA DE AGENDAS COMO PARÂMETRO E ESCREVE OS DADOS NO CSV'''
 
    cabecalho = ["data", "hora", "tipo","descricao", "participantes", "recursos"]
    with open("agendas.csv", "w", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        '''faz uma repetição para escrever no csv as informações lidas'''
        for agenda in lst_agendas:
            escritor.writerow({"data": agenda.data,
                               "hora": agenda.hora, 
                               "tipo": agenda.tipo,
                               "descricao": agenda.descricao, 
                               "participantes": agenda.participantes, 
                               'recursos': agenda.recursos})


def escrever_usuario(lst_usuarios):
    '''DEFINE UM CABEÇALHO PADRAO PARA NAO CAUSAR ERROS NO CARREGAR_USUARIOS
    TODA VEZ QUE É CHAMADA ESSA FUNÇÃO REESCREVE O CABEÇALHO, CASO NAO TER ELA ADD
    RESCEBE A LISTA DE USUARIOS COMO PARAMETRO DE ESCREVE OS DADOS NO CSV'''
    cabecalho = ["nome", "chatId","intervalo_tempo"]
    with open('usuarios.csv', 'w', newline= '') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        '''faz uma repetição para escrever no csv as informações lidas'''
        for usuario in lst_usuarios:
            escritor.writerow({"nome": usuario.nome,
                               "chatId": usuario.chatId,
                               'intervalo_tempo': usuario.intervalo_tempo})


def adicionar_usuario(lst_usuarios):
    '''REALIZA OS INPUTS DOS DADOS DO USUARIO, CRIA O OBJETO USUARIO E ADD NA LISTA DE USUARIOS,
    RETORNA A LISTA DE USUARIOS'''
    while True:
        try:
            nome_usuario = str(input("Insira o nome do usuário: ")).lower()
            chatId = int(input("Insira o chat Id: "))
            intervalo_tempo = int(input("Você quer ser notificado de suas tarefas a cada quantas horas? "))
            usuario = Usuario(nome_usuario,chatId,intervalo_tempo)
            break
        except ValueError:
            print("Nome ou ID inválidos, insira novamente!")
            continue

    lst_usuarios.append(usuario)
    escrever_usuario(lst_usuarios)


def adicionar_agenda(lst_agendas,lst_usuarios):
    '''REALIZA OS INPUTS DE TODOS OS ATRIBUTOS, CRIA O OBJETO AGENDA COM OS ATRIBUTOS, ADD NA LISTA E ATUALIZA O ARQUIVO'''
    '''REALIZA UM LOOP PARA VALIDAR A DATA E HORA CASO DATA INSERIDA FOR ANTES DA DATA ATUAL O PROGRAMA INVALIDA'''
    tipos_agendas = ['compromisso', 'lembrete']
    while True:
        data = input("Insira a data da agenda (DD/MM/AAAA): ")
        hora = input("Insira a hora: ")

        try:
            data = datetime.datetime.strptime(data, "%d/%m/%Y").strftime("%d/%m/%Y")
            hora = datetime.datetime.strptime(hora, "%H:%M").strftime("%H:%M")
            data_atual = datetime.date.today()

            if datetime.datetime.strptime(data, "%d/%m/%Y").date() < data_atual:
                print("Data inválida, Insira novamente!")
                continue
            break
        except ValueError:
            print("Data ou hora inválida, Insira novamente!")
    
    '''verifica na lista de tipos se o tipo inserido é valido'''
    while True:
        agenda_tipo = str(input("Insira o tipo (compromisso/lembrete): ")).lower()
        if agenda_tipo not in tipos_agendas:
            print("Tipo inválido, Insira novamente!")
            continue
        break
    '''realiza o input de outros atributos'''    
    agenda_descricao = str(input("Insira uma descrição: ")).lower()
    agenda_participantes = str(input("Insira os participantes (separados por vírgula): ")).lower().split(",")
    '''realiza a validação do usuário, caso o usuário exista nos arquivos ele add o lembrete
    caso nao exista ele da usuário inválido
    O nome do usuário não é inserido, ele é utilizado apenas para comparar, o que é salvo na agenda é o chat Id do usuário'''
    participantes_validos = validar_usuario(agenda_participantes, lst_usuarios)
    if participantes_validos is None:
        print("Usuário inválido, insira novamente!")
        return
    else:
        agenda_participantes = participantes_validos    

    agenda_recursos = str(input("Insira os recursos (separados por vírgula): ")).lower().split(",")
    '''cria o objeto e add na lista'''
    agenda = Agenda(data, hora, agenda_tipo, agenda_descricao, agenda_participantes, agenda_recursos)
    lst_agendas.append(agenda)
    escrever_agendas_csv(lst_agendas)


def excluir_agenda(lst_agendas, lst_usuarios):
    '''REALIZA A EXCLUSÃO DE UMA AGENDA DA LISTA, ATUALIZA O ARQUIVO CSV'''
    '''verifica se a lista está vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    
    '''realiza a validação do usuário, caso exista continua
    caso nao exista interrompe a eexecução'''
    participante_encontrado = None
    while True:
        nome_participante = input("Insira o nome do participante: ").lower()
        participante_encontrado = next((usuario for usuario in lst_usuarios if usuario.nome == nome_participante), None)
        if participante_encontrado:
            break
        else:
            print("Usuário não encontrado. Insira novamente.")

    '''salva em uma lista todos os compromissos que tem como participante quem o usuário inseriu
    após realiza validações básicas, caso lista vazia interrompe, caso 1 elemento na lista ele pula a próxima validação'''
    lst_agendas_para_excluir = [agenda for agenda in lst_agendas if str(participante_encontrado.chatId) in agenda.participantes]

    if len(lst_agendas_para_excluir) == 0:
        print("Nenhuma agenda encontrada para o participante fornecido.")
        return

    if len(lst_agendas_para_excluir) == 1:
        lst_agendas = [agenda for agenda in lst_agendas if str(participante_encontrado.chatId) not in agenda.participantes]
       
    else:
        '''caso o usuário tiver mais de uma agenda em seu nome o programa printa todas essas agendas
        numera as agendas  e o usuário pode escolher qual delas excluir'''
        print(f"Foram encontradas {len(lst_agendas_para_excluir)} agendas para o participante fornecido. Selecione a agenda a ser excluída:")
        for i, agenda in enumerate(lst_agendas_para_excluir):
            print(f"{i + 1}. Data: {agenda.data}, Hora: {agenda.hora}, Tipo: {agenda.tipo}, Descrição: {agenda.descricao}, Participantes: {agenda.participantes}, Recursos: {agenda.recursos}")

        escolha = int(input("Digite o número correspondente à agenda que deseja excluir: "))
        if escolha < 1 or escolha > len(lst_agendas_para_excluir):
            print("Escolha inválida.")
            return

        '''seleciona na lista a agenda escolhida e realiza a remoção, após escreve a lista atualizada no csv '''
        agenda_selecionada = lst_agendas_para_excluir[escolha - 1]
        lst_agendas.remove(agenda_selecionada)

    escrever_agendas_csv(lst_agendas)
    print("Agenda excluída com sucesso!")


def alterar_agenda(lst_agendas, lst_usuarios):
    '''ALTERA OS ATRIBUTOS DE UM COMPROMISSO COM O ID INSERIDO PELO USUÁRIO
    PERCORRE A LISTA, E ATUALIZA OS ATRIBUTOS'''

    '''verifica se a lista está vazia'''
    if verifica_lst_vazia(lst_agendas) == False:
        return
    
    '''verifica se o usuário existe nos usuários cadastrados, caso verdade continua o código
    caso falso pede para inserir novamente '''
    participante_encontrado = None
    while True:
        nome_participante = input("Insira o nome do participante: ").lower()
        participante_encontrado = next((usuario for usuario in lst_usuarios if usuario.nome == nome_participante), None)
        if participante_encontrado:
            break
        else:
            print("Usuário não encontrado. Insira novamente.")

    '''usa uma repetição para procurar se o usuário informado tem agendas/compromissos marcados
    caso verdadeiro salva todas numa lista, caso nao achar envia a mensagem e retorna
    caso tiver apenas 1 agenda o programa ja pula a outra validação e altera os atributos '''
    lst_agendas_para_alterar = [agenda for agenda in lst_agendas if str(participante_encontrado.chatId) in agenda.participantes]
    if not lst_agendas_para_alterar:
        print("Nenhuma agenda encontrada para o participante fornecido.")
        return

    if len(lst_agendas_para_alterar) == 1:
        agenda_alterar = lst_agendas_para_alterar[0]

    else:
        '''caso o usuário tiver mais de uma agenda o programa printa todas e pergunta qual tem que ser alterada
        faz a numeração de cada uma e pede para o usuário informar qual quer mudar'''
        print(f"Foram encontradas {len(lst_agendas_para_alterar)} agendas para o participante fornecido. Selecione a agenda a ser alterada:")
        for i, agenda in enumerate(lst_agendas_para_alterar):
            print(f"{i + 1}. Data: {agenda.data}, Hora: {agenda.hora}, Tipo: {agenda.tipo}, Descrição: {agenda.descricao}, Participantes: {agenda.participantes}, Recursos: {agenda.recursos}")

        escolha = int(input("Digite o número correspondente à agenda que deseja alterar: "))
        if escolha < 1 or escolha > len(lst_agendas_para_alterar):
            print("Escolha inválida.")
            return
        
        '''acha na lista de agendas do usuário qual ele quer alterar'''
        agenda_alterar = lst_agendas_para_alterar[escolha - 1]

    '''realiza uma repetição para pedir ao usuario informar qual atributo mudar'''
    while True:
        printar_agenda(agenda_alterar)
        print("\nEscolha o atributo que deseja alterar:")
        print("1- Data\n2- Hora\n3- Tipo\n4- Descrição\n5- Recursos")
        '''repetição para escanear as escolhas e fazer validação dos valores inseridos
        caso valor inválido, o programa pede novamente'''
        try:
            escolha = int(input("Digite o número correspondente ao atributo que deseja alterar: "))
        except ValueError:
            print("Atributo inválido. Insira novamente!")
            continue

        if escolha == 1:
            while True:
                nova_data = input("Insira a nova data da agenda (DD/MM/AAAA): ")
                try:
                    datetime.datetime.strptime(nova_data, "%d/%m/%Y")
                    agenda_alterar.data = nova_data
                    break
                except ValueError:
                    print("Data inválida. Insira novamente!")
        elif escolha == 2:
            while True:
                nova_hora = input("Insira a nova hora da agenda (HH:MM): ")
                try:
                    datetime.datetime.strptime(nova_hora, "%H:%M")
                    agenda_alterar.hora = nova_hora
                    break
                except ValueError:
                    print("Hora inválida. Insira novamente!")
        elif escolha == 3:
            tipos_agendas = ['compromisso', 'lembrete']
            while True:
                novo_tipo = input("Insira o novo tipo da agenda (compromisso/lembrete): ").lower()
                if novo_tipo not in tipos_agendas:
                    print("Tipo inválido. Insira novamente!")
                else:
                    agenda_alterar.tipo = novo_tipo
                    break
        elif escolha == 4:
            nova_descricao = input("Insira a nova descrição da agenda: ")
            agenda_alterar.descricao = nova_descricao
        elif escolha == 5:
            novos_recursos = input("Insira os novos recursos da agenda (separados por vírgula): ")
            agenda_alterar.recursos = novos_recursos.lower().split(",")
        else:
            print("Escolha inválida.")
            return

        '''atualiza o csv com as novas informações a cada alteração '''
        escrever_agendas_csv(lst_agendas)
        print("Agenda alterada com sucesso!")
        printar_agenda(agenda_alterar)
        '''pergunta ao usuário se quer alterar mais algum atributo
        caso verdadeiro continua o loop
        caso falso para a função'''
        while True:
            try:
                continuar = int(input("Deseja alterar mais algum atributo? (1- Sim) (2- Não): "))
                if continuar == 1:
                    break
                elif continuar == 2:
                    return
                else:
                    print("Escolha inválida. Insira novamente!")
            except ValueError:
                print("Escolha inválida. Insira novamente!")
