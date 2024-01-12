"""
Calcula a media da idade de um conjunto de professores
"""
"""
count_nomes = int(input("Quantos professores? "))
count_n=0
acum_idade=0
# Repetição clássica com contador
while count_n<count_nomes:
    nome_prof=input('Nome do professor: ')
    idade=int(input('Idade do professor'))
    acum_idade+=idade
    count_n+=1
avg_idade=acum_idade/count_nomes
print('Media de idade dos professores: {}'.format(avg_idade))

#Repetição com teste de valor lido
nome_prof=input('Nome do professor: ')
acum_idade=0
count_nomes=0
while nome_prof!='':
    idade=int(input('Idade do professor'))
    acum_idade+=idade
    #count_nomes=count_nomes+1
    count_nomes+=1
    nome_prof = input('Nome do professor: ')
else:
    print('Foram informados {} professores'.format(count_nomes))
avg_idade=acum_idade/count_nomes
print('Media de idade dos professores: {}'.format(avg_idade))
"""
# Loop usando for
# Itera sobre um objeto, armazenando na variável cada elemento
valores=list(range(3))
print(valores)
for i in valores:
    print(i, ' ', end='')
print(i)

# Break permite descontinuar o laço
for i in range(1,10,2):
    if i==7:
        break
    print(i, ' ', end='')
print('')

# Continue permite pular instruções e voltar ao loop
for i in range(1,10):
    if i%2==0:
        continue
    print(i, ' ', end='')

