"""
- Tuplas são imutáveis e tem tamanho fixo, desta forma não é possível adicinar itens
- Assim como as listas são coleções de objetos ordenados, acessados por deslocamento
- Podem ser criadas sem parênteses, chaves ou colchetes
"""

tup1 = 10, 15, 25
print('Valores de tup1:', tup1)
tup2 = (5*3), (4/2), 75/3
print('Valores de tup2: ', tup2)
print('Tipo de tup1: ', type(tup1))
print('Valor do segundo elemento: ', tup1[1])

print('Iterando em tup1')
# Iteração em tuplas
for t1 in tup1:
    print(t1)

# Tuplas também podem ter elementos de diferentes tipos
tup3 = (5, 'teste', 12)
print('Valores de tup3: ', tup3)

# Tuplas podem ter listas aninhadas
times_tp = 'inter', 'gremio', ['atletico', 'cruzeiro']
print('Valores e tipo de times_sp:', times_tp, type(times_tp))

# Em diversas situações uma atribuição de parte de um objeto gera uma referência para objeto de outro tipo
times_mg = times_tp[2]
print('Valores e tipo de times_mg: ', times_mg, type(times_mg))

# Método que conta quantas vezes um elemento aparece.
print('Contagem de times_tp: ', times_tp.count('inter'))

# É possível converter uma tupla em lista
times_lst = list(times_tp)
print('Conversão para lista: ', times_lst, type(times_lst))

# Tuplas não podem ser alteradas inplace. Tuplas são sequencias imutaveis
# times_tp[0] = 'juventude'

# Desempacotar objetos
time1, time2, time3 = times_tp
print('Objetos separados: ', time1, time2)
time_mg1, time_mg2 = times_mg
print('Objetos separados times_mg: ', time_mg1, time_mg2)

# Tuplas nomeadas, usadas como registros
# Uso do pacote collections
from collections import namedtuple
Pessoa = namedtuple('Pessoas', 'nome idade endereco cpf medidas')
pessoa1 = Pessoa('Evandro', 49, 'Rua X', '99999', (1.87, 110))
print(pessoa1)
print(pessoa1.nome)
print(pessoa1[1])
print(pessoa1.medidas[0])
nome, idade, *dados_restantes = pessoa1
print(nome, idade, dados_restantes)

