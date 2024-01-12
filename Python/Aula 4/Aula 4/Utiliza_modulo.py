# Importando tudo o que está no pacote
#from Modulo_calc import *

#print(f_calc_soma(10, 20))
#print(f_calc_mult(20,30))
#print(z)
#z=30
#print(z)

# Importando apenas uma função
#from Modulo_calc import f_calc_potencia
#print(f_calc_potencia(2,3))
#print(f_calc_soma(10, 20))

# Importação do pacote
import Modulo_calc
#print(f_calc_soma(10, 20))
print(Modulo_calc.f_calc_soma(10, 20))
print(Modulo_calc.f_calc_mult(20,30))
z=15
Modulo_calc.z=50
print(Modulo_calc.z)
print(z)
print(Modulo_calc.lista)


