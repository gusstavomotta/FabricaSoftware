"""
Outros exemplos de uso de funções recursivas
A primeira é recursão infinita
A segunda é fibonacci
Exemplo da execução de fibonacci
fib(5) -> fib(4)+fib(3)
          3+2=5
fib(4) -> fib(3)+fib(2)
          2+1=3
fib(3) -> fib(2)+fib(1)
           1+1=2
fib(2) -> fib(1)+fib(0)
          1+0=1
fib(1) -> 1

fib(0) -> 0
"""
# Função recursiva que nunca termina
def recursao_sempre(num):
    recursao_sempre(num+1)

# Inicia em 1 vai aumentando sempre
#res=recursao_sempre(1)

# Fibonacci

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

res = fibonacci(5)
print(res)

