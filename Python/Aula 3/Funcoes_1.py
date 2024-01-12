"""
Exemplos de funções
"""
# Retorna as letras em comum em duas palavras
def letras_comuns(palavra1, palavra2):
    """
    Função que verifica quais letras existem nas duas palavras
    :param palavra1: Primeira palavra
    :param palavra2: Segunda palavra
    :return: Lista com letras em comum
    """
    intersec=[]
    for l1 in palavra1:
        if l1 in palavra2:
            intersec.append(l1)
    return intersec

print(letras_comuns('Evandro', 'Martina'))
# Acesso a documentação da função
print(letras_comuns.__doc__)

# É possível passar qualquer objeto iterável
res=letras_comuns((1, 3, 5,6), (2, 3, 6, 8))
print(res)

#Passando como parâmetro objetos não iteráveis
res = letras_comuns(10, 20)
print(res)


