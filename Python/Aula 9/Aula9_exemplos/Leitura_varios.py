"""
Exemplo que abre dois arquivos
Faz a leitura dos dados de ambos
"""
import fileinput

with fileinput.input(files=('C:\Documentos\Fabrica_software\Aulas\dados_exemplo.txt',
                            'C:\Documentos\Fabrica_software\Aulas\dados_exemplo_1.txt'), encoding='utf8') as file:
    for line in file:
        print(line, end='')

