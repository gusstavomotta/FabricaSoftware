"""
Manipulação de dados no formato pickle
Grava e recupera objetos
"""
import pickle

imoveis_p=pickle.load(open('C:\Documentos\Fabrica_software\Aulas\dados_imoveis.pck', 'rb'))
print(imoveis_p)
print(type(imoveis_p))

lst_idades=[30, 40, 55, 65, 70]
pickle.dump(lst_idades, open('C:\Documentos\Fabrica_software\Aulas\idades.pck', 'wb'))

idades_p=p=pickle.load(open('C:\Documentos\Fabrica_software\Aulas\idades.pck', 'rb'))
print(idades_p)
print(type(idades_p))