"""
Listas aninhadas
"""

# Uma lista com listas de times de estados diferentes
times = [['inter', 'gremio'], ['flamengo', 'vasco'], ['palmeiras', 'corinthians', 'santos']]
print('Todos os times ', times)
times_sp=times[2] # Elemento na posição 2 é uma lista, portanto, cria nova lista
print('Times paulistas: ', times_sp)

# Mudar na lista afeta somente referências para a lista
times[2] = ['palmeiras', 'sao paulo']
print('Todos os times novamente ',times)

# timnes_sp aponta para outro objeto que foi criado extraindo um elemento da lista
print('Tipos de objetos ', type(times), type(times_sp))
