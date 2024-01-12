"""
- Dicionário - dict, hash
- Associa um conjunto de chaves com valores
- São coleções de dados não ordenados, acessados pelas chaves e não por posição ou deslocamento
"""
# Cria dicionário
dic1 = {'nome': 'Evandro', 'idade': 48, 'cidade': 'Mato Leitao'}
print('Dicionário: ', dic1)

# Mostra uma informação baseado na chave
print('Idade: ', dic1['idade'])

# Não permite acesso por coordenada...
#print('Valor de dic1[1]: ', dic1[1])

# Não é o que parece
dic1[0] = 'Nenhuma informação'
print('Valor de dic[0]: ', dic1)

# Remove determinado valor
dic1.pop(0)
print('Dcionario após remover: ', dic1)

dic2={'fusca': 1500, 'brasilia': 2000, 'chevete': 3200, 'gol': 4500, 'caravan': 3500}
print('Iteração por chaves')
for k in dic2.keys():
    print('Chave: {}. Valor:{}'.format(k, dic2[k]))

print('Iteração pelo item completo')
for i in dic2.items():
    print('Item: ', i, 'Chave: ', i[0], 'Valor:', i[1])




