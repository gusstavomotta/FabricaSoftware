# Desafio calculadora 2.0
# Gustavo Oliveira da Motta
# Última modificação 26/03/2023

# Função que guarda as operaçoes
def calcula(op):
    # função que realiza as operações com base na operação e nos argumentos passados
    def operacoes(*args):

        if op == '+':
            # soma todos os elementos da lista
            resultado = sum(args)

        elif op == '-':
            # subtrai o argumento na posição 0 pelo argumento na posição 1 e assume o valor do resultado
            resultado = args[0] - sum(args[1:])

        elif op == '*':
            # seta o resultado como 1 e quando o usuario informa um valor o mesmo é multiplicado por 1 e após e multiplicado pelos próximos numeros inseridos dentro de args
            resultado = 1
            for i in args:
                resultado *= i

        elif op == '/':
            # seta o resultado na posição 0 para que o programa divida o primeiro pelo segundo e armazene na posição 0 o resultado
            resultado = args[0]
            for i in range(1, len(args)):
                resultado /= args[i]

        elif op == '^':
            # seta o resultado na posição 0 e eleva o primeiro numero pelo segundo e armazene na posição 0 o resultado
            resultado = args[0]
            for i in range(1, len(args)):
                resultado **= args[i]

        # retorna o resultado final de qualquer uma das operações escolhidas
        return resultado
    # retorna e executa a função operações que armazena o resultado
    return operacoes


def entradaDados():

    # inicialização da lista de números
    listaNumeros = []
    # loop para o usuário ir informando valores até decidir ver o resultado (Enter)
    while True:
        numeros = input("Informe um número ou ENTER para ver o resultado: ")
        if numeros == '':
            break
        # add os valores na lista como inteiros
        listaNumeros.append(int(numeros))
    # retorna a operação e a lista com os valores
    return listaNumeros

print("\nInforme qual operação matemática você quer realizar.")
print(" + Para adição.")
print(" - Para subtração.")
print(" * Para multiplicação.")
print(" / Para divisão.")
print(" ^ Para potenciação.")

# scannea a operação
op = input("\nOperação: ")
# Atribui  lista de numeros os valores que irão retornar da entrada de dados
listaNumeros = entradaDados()
# Atribiu à variável calculadora a função calcula
calculadora = calcula(op)
# Atribuiu à variavel resultado a varíavel função calculadora passando a lista de números, assim o programa insere a lista de números, verifica qual operação é para realizar e informa o resultado
resultado = calculadora(*listaNumeros)
# Print na tela o resultado final da operação escolhida pelo usuário
print("O resultado é: ", resultado)


# Fim do programa #