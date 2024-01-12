
# Uma lógica interessante que combina string, lista, dicionario
# Aqui é possível ter uma ideia do potencial e do funcionamento de Python
palavras = ['computador', 'televisao', 'notebook', 'smartphone', 'tv portatil', 'computador mesa']

letras = {}

for palavra in palavras:
  letrainicial = palavra[0]
  if letrainicial not in letras:
    letras[letrainicial] = palavra
  else:
    letra_lst = []
    letra_lst.append(letras[letrainicial])
    letra_lst.append(palavra)
    letras[letrainicial]=letra_lst

print(letras)