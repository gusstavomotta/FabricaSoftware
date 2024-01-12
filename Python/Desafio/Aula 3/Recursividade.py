# DESAFIO PYTHON AULA DIA 03/04/2023
# GUSTAVO OLIVEIRA DA MOTTA
# DATA DE MODIFICAÇÃO: 31/03/2023

# INICIALIZA A LISTA COM OS VALORES
listaNumeros = [10, 20, 40, 60, 70, 80, 120]
# FAZ O SCAN DO NUMERO QUE O USUÁRIO INFORMAR
numero = int(input("Insira um valor: "))


def maiorNormal(listaNumeros, numero):

    # CIRA A LISTA QUE VAI ARMAZENRAR OS VALORES QUE SAO MAIORES
    maior = []
    # FOR LOOP PARA I ACESSAR OS VALORES NA LISTA DO NUMERO
    for i in listaNumeros:
        # SE O I FOR MAIOR QUE O NUMERO INFORMADO O VALOR DE I É COLOCADO NA LISTA MAIOR
        if i > numero:
            maior.append(i)
        else:
            continue
    # REOTRNA A LISTA COM OS VALORES
    return maior


def maiorRecursivo(numero, listaNumeros):

    # CRIA A LISTA QUE VAI ARMZENAR OS VALORES QUE SAO MAIORES
    maior = []

    # VERIFICA SE A LISTA ESTÁ VAZIA
    if not listaNumeros:
        return maior

    # COMPARA A LISTA DE NUMEROS NA POSIÇÃO 0 COM O NUMERO INFORMADO PELO USUÁRIO
    elif listaNumeros[0] > numero:
        # CASO IF FOR VERDADEIRO O VALOR ARMAZENADO NA RESPECTIVA POISÇÃO É ARMAZENADO NA LISTA MAIOR[]
        maior.append(listaNumeros[0])

    # REALIZA A RECURSIVDADE
    maior += maiorRecursivo(numero, listaNumeros[1:])
    return maior

# tempo de execução do For loop
# 66.3 ns ± 0.942 ns per loop
maior = maiorNormal(listaNumeros, numero)
# tempo de execução da recursividade
# 116 ns ± 35.8 ns per loop
maiorNum = maiorRecursivo(numero, listaNumeros)
print(maior)
print(maiorNum)
print(listaNumeros)
