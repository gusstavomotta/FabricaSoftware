def f_carrega_dados():
    with open('C:\\Documentos\\IA\\Dataminig\\classif\\precos_imoveis_sc.csv') as arquivo:
        linhas = arquivo.readlines()

        imoveis = []

        for linha in linhas:
            # separa os valores dos campos
            valores = linha[:-1:].split(',')
            # Armazena os dados em um dicionário com os nomes dos atributos
            imovel = {'tamanho': int(valores[0]), 'bairro': int(valores[1]), 'quartos': int(valores[2]), 'banheiros': int(valores[3]), 'andar': int(valores[4]), 'preco': int(valores[5])}
            # Adiciona cada dicionário na lista
            imoveis.append(imovel)
    return imoveis

def f_preco_medio(imoveis):

    preco = [int(imovel['preco']) for imovel in imoveis]
    preco_medio = sum(preco) / len(preco)
    return preco_medio

def mostra_mais_barato(imoveis):
    im = imoveis[0]
    print(im)
    preco_menor=im['preco']
    for im in imoveis:
        preco=im['preco']
        if preco<=preco_menor:
            preco_menor=preco
            tam_menor=im['tamanho']
            bai_menor=im['bairro']
    print('Dados menor: ', tam_menor, bai_menor, preco_menor)

def mostra_mais_caro(imoveis):
    im = imoveis[0]
    preco_maior=im['preco']
    for im in imoveis:
        preco=im['preco']
        if preco>=preco_maior:
            preco_maior=preco
            tam_maior=im['tamanho']
            bai_maior=im['bairro']
    print('Dados maior: ', tam_maior, bai_maior, preco_maior)

def f_media_cont_bairros(imoveis):
    imoveis_bairro = {}
    precos_bairro = {}
    for imovel in imoveis:
        bairro = imovel['bairro']
        if bairro not in imoveis_bairro:
            imoveis_bairro[bairro] = 0
            precos_bairro[bairro] = 0
        imoveis_bairro[bairro] += 1
        precos_bairro[bairro] += int(imovel['preco'])
    precos_medios_por_bairro = {bairro: precos_bairro[bairro] / imoveis_bairro[bairro] for bairro in imoveis_bairro}
    return imoveis_bairro, precos_medios_por_bairro
