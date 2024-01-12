"""
O uso de with permite fazer a leitura dentro do contexto da abertura do arquivo
"""
#with open('C:\Documentos\Fabrica_software\Aulas\dados_exemplo.txt', 'r', encoding='utf8') as file:
#    for line in file:
#        print(line, end='')

# Cria uma lista com as linhas do arquivo
with open('C:\Documentos\Fabrica_software\Aulas\dados_exemplo.txt', 'r', encoding='utf8') as file:
    lst_lines=[line[:-1:] for line in file]

print(lst_lines)
for l in lst_lines:
    atributos=l.split(',')
    print('Nome:', atributos[1])
    print('Idade:', atributos[2])

file.close()



