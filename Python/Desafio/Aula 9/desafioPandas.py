MAX = 99999999
MIN = 0

import pandas as pd

imoveis =pd.read_csv('C:\\Users\\Gustavo Motta\\Desktop\\Pasta vscode\\Python\\Aula 9\\precos_imoveis.csv', sep=',')
infoImoveis = imoveis.values
listaImoveis = []

for linha in infoImoveis:
    
    imovel = {'Tamanho': linha[0], 'Bairro': linha[1], 'Quartos': linha[2], 'Banheiros': linha[3], 'Andar': linha[4], 'Preco': linha[5]}
    listaImoveis.append(imovel)

def calcula_mais_caro(listaImoveis):

    maisCaro = MIN
    for imovel in listaImoveis:
        if maisCaro < imovel["Preco"]:
            maisCaro = imovel["Preco"]
            imovelMaisCaro = imovel

    print("\nImóvel mais caro: ")
    print(imovelMaisCaro)

def calcula_mais_barato(listaImoveis):

    maisBarato = MAX
    for imovel in listaImoveis:
        if maisBarato > imovel["Preco"]:
            maisBarato = imovel["Preco"]
            imovelMaisBarato = imovel
    
    print("\nImóvel mais barato: ")
    print(imovelMaisBarato)

def calcula_media_preco(listaImoveis):

    soma = MIN
    for i in listaImoveis:
        soma = soma + i['Preco'] 

    media = soma / len(listaImoveis)
    print("\nA média de preço dos imóveis é de R$", int(media))

def conta_calcula_media_por_bairro(listaImoveis):

    count1 = MIN
    count2 = MIN
    count3 = MIN
    soma1 = MIN
    soma2 = MIN
    soma3 = MIN

    for i in listaImoveis:

        if i["Bairro"] == 1:
            count1 +=1
            soma1 += i["Preco"]
        
        elif i["Bairro"] == 2:
            count2 +=1
            soma2 += i["Preco"]
        
        else:
            count3 +=1
            soma3 += i["Preco"]

    soma1 = int(soma1 / count1)
    soma2 = int(soma2 / count2)
    soma3 = int(soma3 / count3)

    print(f"\nExistem {count1} imóveis no bairro 1 e a média de valor é R$ {soma1}")
    print(f"Existem {count2} imóveis no bairro 2 e a média de valor é R$ {soma2}")
    print(f"Existem {count3} imóveis no bairro 3 e a média de valor é R$ {soma3}")
 
calcula_mais_caro(listaImoveis)
calcula_mais_barato(listaImoveis)
calcula_media_preco(listaImoveis)
conta_calcula_media_por_bairro(listaImoveis)
