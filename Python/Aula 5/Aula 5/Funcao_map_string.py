import string


def remove_pont(str):
    if str not in string.punctuation:
        return str
    else:
        return ''

frase='Ola. Eu, sou o professor Evandro!'

# Converte em lista o resultado de map
letras=list(map(remove_pont, frase))

#Junta novamente em uma frase
frase_sp=''.join(letras)

print(frase_sp)