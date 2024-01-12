# Referencias para objetos de escopo interno
import builtins
print(dir(__builtins__))
print(zip)

# Escopo aninhado em funções
nome='Evandro'

def mostra_nome():
    #print(nome)
    nome='Joãozinho'
    def mostra_nome2():
        nome='Juca Bala'
        print(nome)
    mostra_nome2()
    print(nome)



mostra_nome()
print(nome)

# Funções retornando funções
def mostra_nome():
    nome='Joãozinho'
    def mostra_nome2():
        nome='Juca Bala'
        print(nome)
    return mostra_nome2

acao = mostra_nome()
print(type(acao))
acao()