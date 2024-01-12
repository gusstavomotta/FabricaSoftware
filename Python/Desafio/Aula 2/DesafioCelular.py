"""
Pedir ao usuario: Se tem celular e qual plataforma
Leitura de dados > armazenar em listas
Percorrer as listas e calcular os indicadores
Mostrar os resultados
"""

# inicilalização
listaAlunos = []
listaSerie = []
listaCelular = []
listaSO = []
listaRAM = []
listaArmazenamento = []
# inicialização dos contadores, todos setados a 0
contaPrimeiro = 0
contaSegundo = 0
contaTerceiro = 0
temCelular = 0
semCel = 0
android = 0
ios = 0
outro = 0
semCelTerceiro = 0
semCelSegundo = 0
semCelPrimeiro = 0

# pede o numero de alunos
numAlunos = int(input('Qual o número de alunos: '))
listaAlunos.append(numAlunos)
cont = 1

# regula a quantidade de repetições utilizando o numAlunos
while numAlunos >= cont:

    anoSerie = input(
        "Em qual ano/série você está matriculado? (primeiro/segundo/terceiro): ")

    # valida a resposta do usuário e adiciona no contador respectivo
    if anoSerie == 'primeiro':
        contaPrimeiro = contaPrimeiro + 1
        listaSerie.append(anoSerie)
    elif anoSerie == 'segundo':
        contaSegundo = contaSegundo + 1
        listaSerie.append(anoSerie)
    elif anoSerie == 'terceiro':
        contaTerceiro = contaTerceiro + 1
        listaSerie.append(anoSerie)

    temCel = input('Possui celular/smartphone? (s/n): ')
    # valida se a resposta for positiva, caso positiva executa os comandos dentro do if
    if temCel == 's':
        temCelular = temCelular + 1
        listaCelular.append(temCel)

        # pergunta qual o sistema operacional utilizado pelo usuario e incrementa o contador
        sisop = input('Qual o sistema operacional? (Android/Ios/Outro): ')
        if sisop == 'android':
            android = android + 1
            listaSO.append(sisop)

        elif sisop == 'ios':
            ios = ios + 1
            listaSO.append(sisop)

        elif sisop == 'outro':
            outro = outro + 1
            listaSO.append(sisop)
        # pergunta a quantidade de Ram
        ram = int(input("Qual a quantidade de RAM disponível?: "))
        listaRAM.append(ram)
        # pergunta a quantidade de armazenamento
        armazenamento = int(
            input("Qual a quantidade de armazenamento interno disponível?: "))
        listaArmazenamento.append(armazenamento)
    # caso reposta o if negativa executa o elif e adiciona no contador de cada série
    elif temCel == 'n':
        if anoSerie == "primeiro":
            semCelPrimeiro = semCelPrimeiro + 1
            semCel += 1

        elif anoSerie == 'segundo':
            semCelSegundo = semCelSegundo + 1
            semCel += 1

        elif anoSerie == 'terceiro':
            semCelTerceiro = semCelTerceiro + 1
            semCel += 1

    cont = cont+1

# printa todas as informações
print("~~~~~~~~~ Informações gerais ~~~~~~~~~~ ")
print("Número total de alunos : ", numAlunos)
print("Número total de alunos que tem celular : ", temCelular)
print("Número total de alunos que não tem celular : ", semCel)
# calcula as porcentagens e printa
print("~~~~~~~~~~ Portcentagens ~~~~~~~~~~")
print(
    f"Porcentagem de alunos com android : {android} ({100*android/numAlunos:.2f}% )")
print(f"Porcentagem de alunos com IOS : {ios} ({100*ios/numAlunos:.2f}%)")
print(
    f"Porcentagem de alunos com Outro SO : {outro}({100*outro/numAlunos: .2f}% )")
# porcentages por turma
print("~~~~~~~~~~ Não possuem celular em cada série/ano ~~~~~~~~~~")
print(f"Primeiro ano: ({100*semCelPrimeiro /contaPrimeiro: .2f}% )")
print(f"Segundo ano: ({100* semCelSegundo/contaSegundo: .2f}% ) ")
print(f"Terceiro ano: ({100*semCelTerceiro/contaTerceiro: .2f}% )")
print("~~~~~~~~~~ Média geral ~~~~~~~~~~")
print(f"Média geral de RAM : {sum(listaRAM)/len(listaRAM): .2f} GB")
print(
    f"Média geral de armazenamento :{(sum(listaArmazenamento)/ len(listaArmazenamento)): }GB")
