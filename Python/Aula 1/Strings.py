# Importando o pacote string
import string
nome_prof='Evandro'
nome_disc='Fabrica de software'
ch_disc=80

# para concatenar um inteiro é necessário converter
print('Disciplina '+nome_disc+' possui '+str(ch_disc)+' horas')
# Método format permite mostrar dados de strings formatadas, com alinhamento
print('Esquerda:| {:<25}|'.format(nome_prof)) # esquerda
print('Direita :| {:>25}|'.format(nome_prof)) # direita
print('Centro  :| {:^25}|'.format(nome_prof)) # centro

# Uso de templates
template = string.Template('$professor é o professor de $disciplina')
print(template.substitute(professor=nome_prof, disciplina=nome_disc))

# Fatiamento de strings
prof_disc = nome_prof[:3]+'_'+nome_disc[:3]
print(prof_disc)
