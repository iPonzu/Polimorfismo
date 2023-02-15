from Personagem import Personagem


class Mago(Personagem):
    def conjurar_magia(self):
        print(f'{self.nome} lança uma magia aleatória')

p6 = Mago('Gandalf', 1000, 1000)
print(p6)
p6.conjurar_magia()

def upgrade_vida(self):
    self.vida += 5

p6.upgrade_vida()
print(p6)   