
class pessoa:
    """
    Classe pessoa
    Atributos: nome, idade e sexo (que não pode ser acessado fora da classe)
    Métodos: Construtor, str que retorna objeto como string e faixa que retorna a faixa de idade
    """
    def __init__(self, p_nome, p_idade, p_sexo):
        self.nome=p_nome
        self.idade=p_idade
        self._sexo=p_sexo

    def __str__(self):
        return 'Nome: {} - Idade: {} - Sexo: {}'.format(self.nome, self.idade, self._sexo)

    def setIdade(self, p_idade):
        self.idade=p_idade

    def getSexo(self):
        if self._sexo=='M':
            return 'Masculino'
        else:
            return 'Feminino'

    def faixaidade(self):
        if self.idade<=18:
            return 'Jovem'
        elif self.idade<=50:
            return 'Adulto'
        else:
            return 'Idoso'

print(pessoa.__doc__)
p1=pessoa('Evandro', 50, 'M')
p2=pessoa('Fulano', 50, 'M')
print(p1)
print(p1.nome)
p1.nome='Teste'
print(p1)
print(p1.getSexo())
print(p1.faixaidade())
p1.idade=15
print(p1.faixaidade())
p1.nome=100
print(p1)
print(type(p1.nome))
