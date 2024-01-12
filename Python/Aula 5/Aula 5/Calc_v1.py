from Modulo_calc import *
#dados=leitura_dados()
dados=leitura_dados_mais()
#resultado=calcula(dados)
#print(resultado)
funcao=calcula_mais(operacao=dados[4])
print(funcao(dados[0], dados[1], dados[2], dados[3]))