import pandas as pd

class Pet:

    """cria a classe pet 
    """
    def __init__(self, codigo, nome, idade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Codigo: {} / Nome: {} / Idade: {}".format(self.codigo, self.nome, self.idade)

        """
        carrega os dados do pet e cria um dicionario com os valores retirados da lista
        """
def carregar_dados_pets():

    pets = pd.read_csv('C:\\Users\\Gustavo Motta\\Desktop\\Pasta vscode\\Python\\Desafio\\Aula 11\\pets.csv', sep=',')
    infoPets = pets.to_dict('records')
    listaPets = []
    for i in infoPets:
        pet = Pet(i["Codigo"], i[" Nome"], i[" Idade"])
        listaPets.append(pet)

    return listaPets

"""Realiza a busca binária"""
def realizar_busca(listaPets):
    
    minimo = 0
    maximo = len(listaPets) - 1
    codigoPet = int(input("Informe o código do PET: "))
    
    #Realiza um while para ir divindo o código em 2, compara se o codigo inserido é maior ou menor que o código que está no meio
    # e vai dividindo até encontrar o valor procurado
    while minimo <= maximo:
        meio = (minimo + maximo) // 2
        valor_meio = listaPets[meio]

        if valor_meio.codigo == codigoPet:
            return meio,valor_meio
        
        elif valor_meio.codigo < codigoPet:
            minimo = meio + 1
            
        else:
            maximo = meio - 1

    return -1

#cria a lista pets e pega a posição da lista e as informações do pet procurado
listaPets = carregar_dados_pets()
posicao, pet = realizar_busca(listaPets)
print(f"O PET está na posição {posicao} da lista.\nInformações do pet: {pet}")

