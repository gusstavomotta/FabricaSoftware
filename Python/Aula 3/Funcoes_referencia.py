"""
Armazenamento de funções em variáveis
"""
# Cria a função
def mostra_mens(var1):
    print('Valor do parâmetro da função: ', var1)

# Armazena em variável uma referência para a função
func = mostra_mens
#Executa a função através da variável
func(10)
