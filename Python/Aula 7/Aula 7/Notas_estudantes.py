class notas_estudantes():
    """
    Classe que implementa uma lista de notas
    Método __len__ permite o uso da função len() como em qualquer lista
    Método __getitem__ habilita o acesso a um conteúdo de uma posição lista[0], por exemplo
    """
    def __init__(self):
        self.lista_notas=[]
        self.melhor_nota=0
        self.pior_nota=11

    def inclui_nota(self, nota):
        self.lista_notas.append(nota)
        if nota>self.melhor_nota:
            self.melhor_nota=nota
        else:
            if self.pior_nota>nota:
                self.pior_nota=nota

    def __len__(self):
        return len(self.lista_notas)

    def __getitem__(self, item):
        return self.lista_notas[item]

    def mostra_melhor(self):
        print('A melhor nota é: ', self.melhor_nota)

    def mostra_pior(self):
        print('A pior nota é: ', self.pior_nota)


turma1=notas_estudantes()
turma1.inclui_nota(9)
turma1.inclui_nota(3)
turma1.inclui_nota(7)

print(len(turma1))
turma1.mostra_pior()
turma1.mostra_melhor()

print(turma1[1])