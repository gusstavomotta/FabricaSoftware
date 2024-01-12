# Variáveis são referências para objetos
var1 = 10
var2 = 15
# var3 aponta para o mesmo objeto apontado por var1
var3 = var1
print(var1, var2, var3)
# var1 passa a pontar para outro objeto
var1=5
print(var1, var2, var3)
print(type(var1), type(var2), type(var3))
# Não há restrição de tipo, var1 muda para uma string
var1 = 'Teste'
print(var1, var2, var3)
print(type(var1), type(var2), type(var3))
#var4='Teste'
var4=var1
print(var1, var4)
print(var1==var4)
print(var1 is var4)
# Cria uma nova string e atribui a var1
# Chama método da classe para retornar nova string a partir da atual
var1=var1.replace('s', 'r')
print(var1, var4)
print(var1.isupper())
