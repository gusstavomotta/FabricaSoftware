"""
Exemplo de herança entre classes
Classe computador é a classe pai
Smartphone herda de computador
"""
class computador:
    """
    Classe pessoa
    Atributos: memória, armazenamento e processador
    Métodos: sitMemoria retorna status de acordo com a quantidade de memória
    """
    def __init__(self, mem, arm, proc):
        self.memoria=mem
        self.armazenamento=arm
        self.processador=proc

    def sitMemoria(self):
        if self.memoria<4:
            return 'Baixa'
        elif self.memoria<8:
            return 'Básica'
        else:
            return 'Boa'

    def __repr__(self):
        class_name=type(self).__name__
        return '{}({!r}, {!r}, {!r})'.format(class_name, self.memoria, self.armazenamento, self.processador)

class smartphone(computador):
    """
       Classe smartphone, herda de computador
       Atributos: tamanho da tela e preço (protegido)
       Métodos: Visor e métodos para retornar e alterar preço
       """
    def __init__(self, mem, arm, proc, tamt):
        self.memoria = mem
        self.armazenamento = arm
        self.processador = proc
        self.tamanhotela=tamt
        self.__preco=0

    def visor(self):
        if self.tamanhotela<4:
            return 'Pequeno'
        else:
            return 'Grande'

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, value):
        if value<0:
            self.__preco=0
        else:
            self.__preco=value



c1=computador(4, 250, 'Celeron 200')
c2=computador(12, 120, 'Pentium 50')
print(c1)
s1=smartphone(4, 64, 'Samsung a1', 6)
print(s1)
print(s1.visor())
s1.preco=100
print(s1.preco)
print(id(c1))
print(id(c2))
print(id(s1))