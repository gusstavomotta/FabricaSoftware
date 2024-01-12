from datetime import datetime
import random
import requests
from tkinter import *


# CRIANDO AS LISTAS E O DICIONÁRIO COM OS FUNCIONÁRIOS
dic_funcionarios = {10: "Gustavo", 20: "Matheus", 30: "Caio", 40: "Victor"}
resolvidas = []
ingnoradas = []
pendentes = []


def cadastro_funcionarios():

    # VALIDAÇÃO DO CÓDIGO E DO NOME DO FUNCIONÁRIO
    valido = False
    while not valido:
        codigoFuncionario = int(input("Insira seu código de funcionario(a): "))
        nome = str(input("Insira seu nome: "))

        if codigoFuncionario in dic_funcionarios.keys():
            if dic_funcionarios[codigoFuncionario] == nome:

                texto_func["text"] = "\nLogin concluído! "
                valido = True

            else:
                texto_func["text"] = "Código e(ou) nome incorreto(s), insira novamente!  "
        else:
            texto_func["text"] = "Código e(ou) nome incorreto(s), insira novamente!  "


def recebe_ocorrencia():

    # FAZENDO O SCAN DAS VARÍAVEIS
    codigo = random.randint(1, 1000)
    dataAtual = datetime.now()
    data = dataAtual.strftime("%d/%m/%Y - %H:%M:%S")
    print("O código da ocorrência é:", codigo)
    print("A data da ocorrência é:", data)
    descricao = str(input("\nInsira a descrição da ocorrência: "))

    # VALIDANDO SE O CÓDIGO DO FUNCIONARIO E O NÍVEL DE GRAVIDADE SÃO VÁLIDOS
    valido = False
    while not valido:

        codigoResponsavel = int(input("Insira o código de funcionário: "))
        nivelGravidade = int(input("Insira o nível de gravidade da ocorrência: (1-5): "))

        if codigoResponsavel in dic_funcionarios.keys():
            if nivelGravidade in range(1, 6):

                # CRIA A LISTA COM OS ATRIBUTOS ESCANEADOS
                ocorrencias = [codigo, data, descricao, codigoResponsavel, nivelGravidade]
                print("\nOcorrência registrada!")
                valido = True

            else:
                print("Código e(ou) nível de gravidade incorretos, insira novamente!")
        else:
            print("Código e(ou) nível de gravidade incorretos, insira novamente!")

    # RETORNA A LISTA
    return ocorrencias


def resolve_ocorrencia(pendentes):

    # VALIDA SE O CÓDIGO DA OCORRÊNCIA EXISTE, MANDA PRA LISTA DE RESOLVIDAS E ADICIONA UMA DESCRIÇÃO APÓS SER RESOLVIDA

    codigo = int(input("Insira o código da ocorrência: "))

    for i in pendentes:
        if codigo == i[0]:

            descrita = str(input("Insira uma descrição: "))
            resolvidas.append(i + [descrita])
            pendentes.remove(i)
            print(f"A ocorrência número {codigo} foi resolvida com sucesso! ")
            return

    print("O código inserido é inválido, realize a operação novamente!")


def ignora_ocorrencia(pendentes):

    # VALIDA SE O CÓDIGO DA OCORRÊNCIA É VÁLIDO COMPARA E MANDA PARA A LISTA DE IGNORADAS

    codigo = int(input("Insira o código da ocorrência: "))
    for i in pendentes:
        if codigo == i[0]:

            ingnoradas.append(i)
            pendentes.remove(i)
            print(f"A ocorrência número {codigo} foi ignorada com sucesso! ")

        return

    print("O código inserido é inválido, realize a operação novamente!")


def consulta_ocorrencia(pendentes):

    # VALIDA SE O CÓDIGO DO FUNCIONÁRIO É VÁLIDO
    valido = False
    while not valido:

        codigo = int(
            input("Insira seu código de funcionario(a) para realizar a consulta: "))
        if codigo in (dic_funcionarios):

            # SE NAO TIVER NADA NA LISTA PRINTA QUE NAO HÁ PENDENCIAS
            if not pendentes:
                print("Nenhuma ocorrência pendente! ")

            # CASO NÃO TIVER PENDÊNDENCIAS PARA O CÓDIGCO INSERIDO PRINTA QUE NÃO HÁ
            elif codigo not in [i[3] for i in pendentes]:
                print(f"Não há ocorrências pendentes para o código {codigo}."),

            valido = True

        else:
            print("Código inválido, digite novamente!")

    # PERCORRE A LISTA DE PENDENCIAS, SE O CÓDIGO FOR 0 PRINTA TODA A LISTA, SE NAO COMPARA O CODIGO COM O CODIGO DA LISTA E REALIZA O PRINT
    consultas = []
    for i in pendentes:

        if codigo == 0:
            print(pendentes)

        elif codigo == i[3]:
            consultas.append(i)

    for i in consultas:
        print(i)


def conta_ocorrencia(pendentes, resolvidas, ignoradas, dic_funcionarios):

    # SETA OS CONTADORES EM 0
    countP = 0
    countR = 0
    countI = 0

    # ESCANEIA O CÓDIGO
    codigo = int(
        input("Informe o código do funcionário que você deseja ver as estatísticas:  "))

    # REALIZA OS LOOPS E INCREMENTA OS CONTADORES
    for i in pendentes:
        if codigo == i[3]:
            countP = countP + 1

    for i in resolvidas:
        if codigo == i[3]:
            countR = countR + 1

    for i in ignoradas:
        if codigo == i[3]:
            countI = countI + 1

    # REALIZA O PRINT DO DICIONÁRIO
    print(
        f"Ocorrencias pendentes do funcionário {dic_funcionarios[codigo]}: {countP}")
    print(
        f"Ocorrencias resolvidas do funcionário {dic_funcionarios[codigo]}: {countR}")
    print(
        f"Ocorrencias ignoradas do funcionário {dic_funcionarios[codigo]}: {countI}")


janela = Tk()
janela.title("Sistema de ocorrências")
janela.geometry("800x600+0+0")

texto_usuario = Label(janela, text= "Clique no botão para abrir o menu.")
texto_usuario.grid(column= 300, row= 400)

botao = Button(janela, text="Cadastrar funcionario", command=cadastro_funcionarios)
botao.grid(column=200, row=300)
texto_func = Label(janela, text=" ")
texto_func.grid(column=200, row= 400)

janela.mainloop()