"""
Leitura de dados de um arquivo texto
Cada linha apresenta dados de pessoas diferentes
A separação é por vírgula
"""
# Abre o arquivo no modo leitura e indica que a codificação é utf8
# Como são usados acentos o padrão retorna caracteres incorretos
file = open('C:\Documentos\Fabrica_software\Aulas\dados_exemplo.txt', 'rt', encoding='utf8')
print('File mode: ', file.mode)
print('File name: ', file.name)

# Acessando as linhas diretamente pelo objeto arquivo
for line in file:
    print(line, end='')
    # Retira o caractere final que é \n
    atributos=line[:-1:].split(',')
    print(atributos)

#file_data=file.read()
#print('Dados do arquivo: ', file_data)

#print('Linhas do arquivo')
#file_lines=file.readlines()
#for line in file_lines:
#    print(line, end='')

file.close()