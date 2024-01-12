"""
Mostra os arquivos de um diretorio
Troca o diretório e mostra novamente
"""

import os
# Mostra o conteúdo do diretorio atual
print('List contents of directory')
print(os.listdir())
# Muda o diretorio
os.chdir('C:\Documentos\Fabrica_software\Aulas')
print('List the updated contents of directory')
print(os.listdir())
