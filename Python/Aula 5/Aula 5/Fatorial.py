"""
Função fatorial em python
Versão recursiva e versão normal
"""

# Exemplo de função que define tipo de parâmetro e retorno
# Opcional, mas pode ser usado em qualquer função python
def fatorial_rec(num: int) -> int:
    if num == 1:
        return 1
    return num * fatorial_rec(num - 1)


fat5 = fatorial_rec(5)
print(fat5)

def fatorial(num: int) -> int:
    res=1
    for v in range(1, num+1):
        print(v)
        res=v*res
    return res

fat5=fatorial(5)
print(fat5)