
def testa_par(x):
    if x%2==0:
        return True
    else:
        return False

counters=[10, 11, 12, 13, 16, 17, 20]

lista_par=list(filter(testa_par, counters))

print(lista_par)

# Equivalente a listcomp

lista_par=[v for v in counters if v%2==0]

print(lista_par)