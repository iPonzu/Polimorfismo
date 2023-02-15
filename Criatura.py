from ast import Or


class Criatura:
    def __init__(self, nome):
        self.nome = nome

    def informacao(self):
        raise NotImplementedError("Subclasse deve implementar o metodo abstrato")

class Orc(Criatura):
    def informacao(self):
        return 'Criatura tribal misteriosa'

class Minotauro(Criatura):
    def informacao(self):
        return 'Criatura que vive nos labirintos'


criaturas = [Orc('Orc 1'), Orc('Orc 2'), Minotauro('Minotauro')]

for criatura in criaturas:
    print(f'Nome: {criatura.nome}, Informações: {criatura.informacao()}')

    