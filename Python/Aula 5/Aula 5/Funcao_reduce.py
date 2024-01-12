from functools import reduce

# Função deve sempre ter dois argumentos
# Neste caso reduce vai usar o atual e o próximo como parâmetros
def inc(x, y):
    return x+y

counters=[1,2,3,4,5]

# Mapeia a soma para a lista de valores
# Vai somar 1+2+3+...
res = reduce(inc, counters)

print(res)

# É possível usar funçãoes anônimas dentro de reduce
res = reduce((lambda x, y: x+y*0.5), counters)

print(res)