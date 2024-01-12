import numpy as np
import pandas as pd


class Atendimento:

    def __init__(self, codigo, data, servico, valor_cobrado):
        self.codigo = codigo
        self.data = data
        self.servico = servico
        self.valor_cobrado = valor_cobrado

    def __str__(self):
        return "Codigo: {} / Data: {} / Seviço: {} / Valor Cobrado: {}".format(self.codigo, self.data, self.servico, self.valor_cobrado)


class Pet:

    def __init__(self, codigo, nome, idade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Codigo: {} / Nome: {} / Idade: {}".format(self.codigo, self.nome, self.idade)


def carregar_dados_atendimentos():

    atendimentos = pd.read_csv(
        'C:\\Users\\Gustavo Motta\\Desktop\\Pasta vscode\\Python\\Desafio\\Aula 11\\atendimentos.csv', sep=',')
    infoAtendimentos = atendimentos.to_dict('records')
    listaAtendimentos = []
    for i in infoAtendimentos:
        atendimento = Atendimento(
            i["Codigo_pet"], i["Data"], i[" Serviço"], i[" Valor_cobrado "])
        listaAtendimentos.append(atendimento)

    print("\nDados carregados com sucesso!")
    return listaAtendimentos


def carregar_dados_pets():

    pets = pd.read_csv(
        'C:\\Users\\Gustavo Motta\\Desktop\\Pasta vscode\\Python\\Desafio\\Aula 11\\pets.csv', sep=',')
    infoPets = pets.to_dict('records')
    listaPets = []
    for i in infoPets:
        pet = Pet(i["Codigo"], i[" Nome"], i[" Idade"])
        listaPets.append(pet)

    return listaPets


def printar_lista(lista):

    print("\n~~~~~~~~ Informações ~~~~~~~~")
    for atendimento in lista:
        print(atendimento)


def calcular_soma_media_por_pet(listaAtendimentos):

    soma  = 0
    soma2  = 0
    soma3  = 0
    soma4  = 0
    soma5 = 0
    count  = 0
    count2  = 0
    count3  = 0
    count4  = 0
    count5 = 0

    for i in listaAtendimentos:

        if i.codigo == 1:
            soma += i.valor_cobrado
            count += 1

        elif i.codigo == 2:
            soma2 += i.valor_cobrado
            count2 += 1

        elif i.codigo == 3:
            soma3 += i.valor_cobrado
            count3 += 1

        elif i.codigo == 4:
            soma4 += i.valor_cobrado
            count4 += 1

        else:
            soma5 += i.valor_cobrado
            count5 += 1

    print("\n~~~~~~~~ Informações Pets ~~~~~~~~")
    print("Cachorro 1: Valor gasto: R$ {:.2f} / Média: R$ {:.2f} / Nº de consultas: {}".format(
        soma, soma/count, count))
    print("Cachorro 2: Valor gasto: R$ {:.2f} / Média: R$ {:.2f} / Nº de consultas: {}".format(
        soma2, soma2/count2, count2))
    print("Cachorro 3: Valor gasto: R$ {:.2f} / Média: R$ {:.2f} / Nº de consultas: {}".format(
        soma3, soma3/count3, count3))
    print("Cachorro 4: Valor gasto: R$ {:.2f} / Média: R$ {:.2f} / Nº de consultas: {}".format(
        soma4, soma4/count4, count4))
    print("Cachorro 5: Valor gasto: R$ {:.2f} / Média: R$ {:.2f} / Nº de consultas: {}".format(
        soma5, soma5/count5, count5))


def ordenar_lista_nome(listaPets):

    for i in range(0, len(listaPets)):
        for j in range(0, len(listaPets) - 1):
            if listaPets[j].nome > listaPets[j+1].nome:
                listaPets[j], listaPets[j+1] = listaPets[j+1], listaPets[j]

    return listaPets


def quick_sort(listaAtendimentos):

    if len(listaAtendimentos) > 1:

        pivo = len(listaAtendimentos) // 2
        valor = listaAtendimentos[pivo]

        esquerda = quick_sort(
            np.array([i for i in listaAtendimentos if i.data < valor.data]))
        meio = np.array([i for i in listaAtendimentos if i.data == valor.data])
        direita = quick_sort(
            np.array([i for i in listaAtendimentos if i.data > valor.data]))

        ret = np.concatenate((esquerda, meio, direita), axis=0)

        return ret

    else:
        return listaAtendimentos

def realizar_busca(listaPets):
    
    minimo = 0
    maximo = len(listaPets) - 1

    codigoPet= int(input("Informe o código do PET: "))
    
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        valor_meio = listaPets[meio]

        if valor_meio == codigoPet:
            return meio
        elif valor_meio < codigoPet:
            minimo = meio + 1
        else:
            maximo = meio - 1

    return -1
