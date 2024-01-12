'''ARQUIVO DEDICADO PARA A CLASSE'''


class Agenda:
    '''CLASSE AGENDA COM OS ATRIBUTOS DE AGENDA'''

    def __init__(self, data, hora, tipo, descricao, participantes=None, recursos=None):

        self.data = data
        self.hora = hora
        self.tipo = tipo
        self.descricao = descricao
        self.participantes = participantes
        self.recursos = recursos

    def __str__(self):
        return "{},{},{},{},{},{},{}".format(self.data, self.hora, self.tipo, self.descricao, self.participantes, self.recursos)


class Usuario:
    '''CLASSE USUARIO COM OS ATRIBUTOS DO USUARIO'''

    def __init__(self, nome, chatId, intervalo_tempo):
        self.nome = nome
        self. chatId = chatId
        self. intervalo_tempo = intervalo_tempo
