
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