idade = input("Idade: ")
altura = input("Altura: ")
peso=input("Peso: ")
print(type(idade))
print(type(altura))
imc = int(peso)/float(altura)**2
# Saída formatada com print
print('Idade: {}. Altura: {} Peso: {} IMC: {}'.format(idade, altura, peso, imc))
