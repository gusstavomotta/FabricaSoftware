"""
- Exemplo de classes derivadas de dict
- Classes disponíveis no pacote collections
"""

from collections import Counter
# Cria um dicionário que mantém cada chave com a contagem correspondente
# Recebe uma lista como parâmetro e automaticamente gera a contagem
cars = Counter(['fusca', 'brasilia', 'gol', 'fusca', 'gol', 'chvete'])
print('Dicionario: ', cars)
# Mostra quantos fuscas existem
print('Número de fuscas: ', cars['fusca'])
# Mostra os dois carros mais comuns
print(cars.most_common(2))







