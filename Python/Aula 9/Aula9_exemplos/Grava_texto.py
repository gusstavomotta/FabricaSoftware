"""
Grava dados em um arquivo texto
Sempre que o arquivo é aberto ele é sobreescrito
"""

file = open('C:\Documentos\Fabrica_software\Aulas\dados_exemplo_1.txt', 'w', encoding='utf8')
file.write('10, João, 17\n')
file.write('20, Maria, 33\n')
file.write('20, Jesus, 2023\n')
file.close()

# Abre o mesmo arquivo para incluir novas linhas
file = open('C:\Documentos\Fabrica_software\Aulas\dados_exemplo_1.txt', 'a', encoding='utf8')
file.write('Fim do arquivo\n')
file.close()
