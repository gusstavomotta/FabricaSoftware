"""#### Coleções
- Listas, arrays, séries, tuplas, dataframe.
- Listas: Objetos mais flexíveis, são mutáveis, permitem acesso por deslocamento e diferentes tipos de daos
- Tuplas: São como registros, permitem valores de diferentes tipos, acesso por deslocamento, mas são imutáveis.
- Dicionários: Baseados em hash table, pares de chave e valor.
- Conjuntos: Formados por valores únicos
- Arrays: Valores somente de um tipo (homogêneos)
"""

# Criação de 3 listas
# Repetição para buscar valores de duas listas e inserir o resultado na terceira
# Identação do código indica bloco de instruções
l1 = [10, 20, 30]
l2 = [1.2, 2.4, 5.5]
l3 = []

# Laço que obtém cada valor da lista
# Listas são estruturas que permitem iteração
for v1 in l1:
  print(v1)
  #print('z')


print('X')

for vl1, vl2 in zip(l1, l2):
  v_calc = vl1*vl2
  #print(vl1, vl2, v_calc)
  l3.append(v_calc)

print(l3)

# Lista podem ter valores de qualquer tipo, tem tamanho variável
# São coleções ordenadas e flexíveis e podem ser aninhadas
# Um recurso que em algumas linguagens exigiria implementação com algum código extra
lista1 = [15, 10, 24, 32]
lista2 =['alto', 100, 'medio', 'baixo']
# lista3 é uma referência para o mesmo objeto referenciado por lista1
lista3 = lista1
print(lista1, lista2, lista3)
lista1[1] = 25
print(lista1, lista3)
# Existem diversos métodos para manipular listas
lista1.sort(reverse=True)
print(lista1, lista3)
#print(type(lista1))
#print(type(lista1[1]))
# Remove um valor da lista e reordena os demais
print(lista2.pop(1))
print(lista2)
# Mudança inplace, altera o objeto o que repercute nas duas referências
# Coordenadas iniciam em 0, por isso 3 é a última
#lista1[3] = 12
#print(lista1, lista3)
# Somar duas listas é simples
#lista1_mais_3 = lista1 + lista3
#print('Lista1_3: ',lista1_mais_3)
# Lista com listas aninhadas
times = [['inter', 'gremio'], ['flamengo', 'vasco'], ['palmeiras', 'corinthians', 'santos']]
print(times)
times_sp=times[2]
print(times_sp)
# Mudar na lista afeta somente referências para a lista
#times[2] = ['palmeiras', 'sao paulo']
#print(times)
# timnes_sp aponta para outro objeto que foi criado extraindo um elemento da lista
#print(times_sp)
#print(type(lista1), type(times), type(times_sp))

# Slice, com indicação de salto
lista_num=list(range(10))
print(lista_num)
print(lista_num[::2])
print(lista_num[::-2])
print(lista_num[2:8:3])

# Tuplas são imutáveis e tem tamanho fixo, desta forma não é possível adicinar itens
# Assim como as listas são coleções de objetos ordenados, acessados por deslocamento
# Podem ser criadas sem parênteses, chaves ou colchetes
tup1 = 10, 15, 25
print(tup1)
tup2 = (5*3), (4/2), 75/3
print(tup2)
print(type(tup1))
print(tup1[1])
# Tuplas também podem ter elementos de diferentes tipos
tup3 = (5, 'teste', 12)
print(tup3)
# Tuplas podem ter listas aninhadas
times_tp = 'inter', 'gremio', ['atletico', 'cruzeiro']
print(times_tp, type(times_tp))
# Em diversas situações uma atribuição de parte de um objeto gera uma referência para objeto de outro tipo
times_mg = times_tp[2]
print(times_mg, type(times_mg))
# Método que conta quantas vezes um elemento aparece.
#print(times_tp.count('inter'))
# É possível converter uma tupla em lista ou outro tipo de objeto
#times_lst = list(times_tp)
#print(times_lst, type(times_lst))
# Tuplas não podem ser alteradas inplace. Tuplas são sequencias imutaveis
times_tp[0] = 'juventude'
# Desempacotar objetos
#time1, time2, time3 = times_tp
#print(time1, time2)
#time_mg1, time_mg2 = times_mg
#print(time_mg1, time_mg2)

# Tuplas nomeadas, usadas como registros
from collections import namedtuple
Pessoa = namedtuple('Pessoas', 'nome idade endereco cpf medidas')
pessoa1 = Pessoa('Evandro', 49, 'Rua X', '99999', (1.87, 110))
print(pessoa1)
print(pessoa1.nome)
print(pessoa1[1])
print(pessoa1.medidas[0])
nome, idade, *dados_restantes = pessoa1
print(nome, idade, dados_restantes)

# Fatiamento de objetos
lista1 = [10000, 15000, 25000, 18000, 13500, 8200]
print(lista1)
# Os dois primeiros, : significa da posição inicial
print('Primeiros: ', lista1[:2])
# Aqui é omitida a posição final e asume-se que vai até a última
# Após as duas primeiras mostra todos
print('Ultimos: ', lista1[2:])
# Definição da posição inicial e final (exlcluida)
print('De 1 a 3: ', lista1[1:3])
# Negativo? A partirda posição final, menos 1
print('E?: ', lista1[-1:])
# Todos a partir da posição inicial menos o último
print('Novamente: ', lista1[:-1])
# Strings podem ser consideradas listas
#nome = 'Evandro'
#print(nome[1:4])
# Percorrendo a lista
#for valor in lista1:
#  print('Valor: ', valor)
# Enumerate devolve posição e o valor
for pos, valor in enumerate(lista1):
  print('Valor: ', pos, valor)

# Dicionário - dict, hash
# Associa um conjunto de chaves com valores
# São coleções de dados não ordenados, acessados pelas chaves e não por posição ou deslocamento
dic1 = {'nome': 'Evandro', 'idade': 48, 'cidade': 'Mato Leitao'}
print(dic1)
# Mostra uma informação baseado na chave
print(dic1['idade'])
# Não permite acesso por coordenada...
#print(dic1[1])
# Não é o que parece
dic1[0] = 'Nenhuma informação'
print(dic1)
#dic1.pop(0)
#print(dic1)

# Gerando um dicionario a partir de listas
codigos = [1, 2, 3]
produtos = ['lapis', 'caneta',  'caderno']
# Dicionario vazio
materiais = {}
# Repetição que combina um elemento de uma lista com outro adiciionando ao dicionario
# zip retorna elementos de listas diferentes
for chave, valor in zip(codigos, produtos):
  materiais[chave] = valor
print(materiais)

# Uma lógica interessante que combina string, lista, dicionario
# Aqui é possível ter uma ideia do potencial e do funcionamento de Python
palavras = ['computador', 'televisao', 'notebook', 'smartphone', 'tv portatil', 'computador mesa']

letras = {}

for palavra in palavras:
  letrainicial = palavra[0]
  if letrainicial not in letras:
    letras[letrainicial] = palavra
  else:
    letra_lst = []
    letra_lst.append(letras[letrainicial])
    letra_lst.append(palavra)
    letras[letrainicial]=letra_lst

print(letras)

# Conjuntos são dicionários sem valores, somente com chaves
# Considerada uma coleção não ordenada de valores únicos
conj1 = {1, 3, 5}
conj2 = {3, 7, 9}
lista_dup = [1, 1, 3,  5, 5, 5, 4, 7, 9]
print(lista_dup)
# A atribuição de uma lista para um conjunto elimina as duplicações
conj3 = set(lista_dup)
print(conj1, conj2, conj3)
# Não é possível acessar por deslocamento
#print(conj1[1])
# Existem várias operações em conjuntos
# Operações tradicinais da teoria matemática dos conjuntos
print(conj1.union(conj2))
print(conj1.intersection(conj2))

# Arrays são alternativas a listas ou outros objetos
# A criação é feita usando alguma biblioteca
# É importada a biblioteca array
import array as arr
# A função recebe como parâmetro inicial o tipo de dado e em seguida os elementos
a1 = arr.array('i', [1, 2, 3, 4, 5])
print(a1[0])
print(a1)
print(type(a1))

# Usando o pacote Numpy (Numerical Python)
# Um dos pacotes mais importantes de Python
import numpy as np
# Gera números aleatórios para um vetor de 4 linhas e 5 colunas
vetor1 = np.random.randn(4,5)
print(vetor1, '\n', type(vetor1))
vet_dobro = vetor1*2
print(vet_dobro)
vetor2 = np.array([10, 15, 25, 50])
print(vetor2)
# Elementos em um vetor tem todos o mesmo tipo. O que acontece neste caso?
vetor3 = np.array([10, 'teste', 20])
print(vetor3)

# Uso de listcompreensions e expressões geradoras
# Em uma linha é possível gerar listas sem uso de repetições tradicionais
frase = 'Estudando Python'
# String é um objeto iterável, assim como listas, tuplas, etc
lista_letras = [l for l in frase]
print(lista_letras)
lista_vogais = [c for c in frase if c in 'aeiouAEIOU']
print(lista_vogais)
