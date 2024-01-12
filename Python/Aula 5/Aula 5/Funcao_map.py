"""
Função de alta ordem map é nativa do Python
Aplica uma função a um conjunto de argumentos (objeto iterável)
"""

from timeit import timeit
counters=[1,2,3,4,5]

def inc(x):
    return x+10

res = list(map(inc, counters))
print(res)
print(map.__doc__)

#Equivalente em listcomps
res = [inc(l) for l in counters]
print(res)

# Usando for...loop
res=[]
for l in counters:
    res.append(inc(l))

print(res)
print(timeit())