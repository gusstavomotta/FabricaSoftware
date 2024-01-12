"""
Uso do pacote pandas
"""

import pandas as pd

imoveis=pd.read_csv('C:\Documentos\Fabrica_software\Aulas\dados_imoveis.csv', sep=',')

print(imoveis)
print(imoveis.describe())

lst_tamanho=list(imoveis.tamanho)

print(lst_tamanho)

imoveis.to_pickle('C:\Documentos\Fabrica_software\Aulas\dados_imoveis.pck')

imoveis.to_json('C:\Documentos\Fabrica_software\Aulas\dados_imoveis.json')