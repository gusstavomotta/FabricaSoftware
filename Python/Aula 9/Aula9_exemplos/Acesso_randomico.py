"""
Grava dados em determinada posição do arquivo
O acesso neste caso é randômico e não sequencial
"""
f = open('C:\Documentos\Fabrica_software\Aulas\ex_random.txt', 'w')
f.write('Disciplina:                      Professor:                            \n')
# Define a posição que os dados serão gravados
f.seek(12,0)
f.write('Fabrica de software')
f.seek(45, 0)
f.write ('Evandro Franzen')

f.close()
with open('C:\Documentos\Fabrica_software\Aulas\ex_random.txt', 'r') as f:
    for line in f:
        print(line, end='')