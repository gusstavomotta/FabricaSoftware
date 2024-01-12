class carro:

    def __init__(self, placa, modelo, marca, valor):

        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.valor = valor

    def __str__(self):
        return 'Placa: {} / Modelo: {} / Marca: {}  / Valor: {}'. format(self.placa, self. modelo, self. marca, self.valor)

    def setPLaca(self, placa):
        self.placa = placa

    def setMOdelo(self, modelo):
        self.modelo = modelo

    def setMarca(self, marca):
        self.marca = marca

    def setValor(self, valor):
        self.valor = valor

lista_carros = []


def adicionar_veiculo(lista_carros):

    placaVeiculo = input("Informe a Placa do veículo: ")
    modeloVeiculo = input("Informe o modelo do veículo: ")
    marcaVeiculo = input("Informe a marca do veículo: ")
    valorVeiculo = float(input("Informe o valor do veículo: "))

    veiculo = carro(placaVeiculo, modeloVeiculo, marcaVeiculo, valorVeiculo)
    lista_carros.append(veiculo)
    print("\nVeículo adicionado ao sistema! ")


def remover_veiculo(lista_carros):

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        placa = input(
            "Qual veículo que você deseja remover do sistema? Informe a placa: ")

        for i in lista_carros:
            if placa == i.placa:
                lista_carros.remove(i)
                print("\nVeículo removido do sistema!")
                return

        print("\nPlaca inválida, insira novamente! ")


def alterar_atributo_veiculo(lista_carros):

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        placa = input(
            "Você deseja alterar os atributos de qual veículo? Informe a placa: ")
        for i in lista_carros:
            if placa == i.placa:
                atributo = input(
                    "Qual atributo você deseja alterar (Placa, Modelo, Marca ou Valor)?: ")

                if atributo == 'placa':
                    altera_atributo = input(
                        "Informe ao sistema a placa atualizada: ")
                    print("\nAlteração conluída!")
                    i.placa = altera_atributo
                    return

                elif atributo == 'modelo':
                    altera_atributo = input(
                        "Informe ao sistema o modelo atualizado: ")
                    print("\nAlteração conluída!")
                    i.modelo = altera_atributo
                    return

                elif atributo == 'marca':
                    altera_atributo = input(
                        "Informe ao sistema a marca atualizada: ")
                    print("\nAlteração conluída!")
                    i.marca = altera_atributo
                    return

                elif atributo == 'valor':
                    altera_atributo = input(
                        "Informe ao sistema o valor atualizado: ")
                    print("\nAlteração conluída!")
                    i.valor = altera_atributo
                    return

                else:
                    print("Atributo informado é inválido, informe novamente!")
                    return

        print("Placa inválida, insira novamente!")


def mostrar_veiculos(lista_carros):

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        print("\nAqui estão todos os veículos cadastrados no sistema: ")
        for i in lista_carros:
            print(i)


def aumentar_preco(lista_carros):

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        try:
            percentual = float(input("Insira o percentual de reajuste: "))
            for i in lista_carros:
                i.valor = (float(i.valor)) + (float(i.valor) * percentual/100)

        except ValueError:
            print("Valor inserido é inválido, tente novamente!")
            return

        print("\nValor reajustado com sucesso!")


def diminuir_preco(lista_carros):

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        try:
            percentual = float(input("Insira o percentual de reajuste: "))
            for i in lista_carros:
                i.valor = (float(i.valor)) - (float(i.valor) * percentual/100)

        except ValueError:
            print("Valor inserido é inválido, tente novamente!")
            return

        print("\nValor reajustado com sucesso!")


def calcular_maior_preco(lista_carros):

    maior_valor = 0
    carro_mais_caro = 0

    if valida_lista_vazia(lista_carros) == True:
        return 0
    else:
        for i in lista_carros:
            if maior_valor < int(i.valor):
                maior_valor = int(i.valor)
                carro_mais_caro = i

        print("\nAqui estão as informaçõs do veículo com o maior valor de mercado: ")
        print(carro_mais_caro)


def valida_lista_vazia(lista_carros):

    if not lista_carros:
        print("\nNão há nenhum veículo cadastrado no sistema! ")
        return True


def __getitem__(item):
    return lista_carros[item]