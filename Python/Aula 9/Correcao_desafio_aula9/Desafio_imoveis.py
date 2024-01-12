"""
Solução para o desafio da aula 9
"""

from Mod_desafio_aula9 import *

imoveis=f_carrega_dados()
#print(imoveis)

mostra_mais_caro(imoveis)

mostra_mais_barato(imoveis)

preco_medio=f_preco_medio(imoveis)
print('Preço médio: ', preco_medio)

imoveis_por_bairro, precos_medios_por_bairro=f_media_cont_bairros(imoveis)


print('Contagem e preço médio dos imóveis por bairro:')
for bairro, contagem in imoveis_por_bairro.items():
    print(f'Bairro {bairro} possui {contagem} imóveis com preço médio= {precos_medios_por_bairro[bairro]}')