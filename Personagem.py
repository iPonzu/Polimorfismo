class Personagem:
    def __init__(self, nome, idade, vida):
        self.nome = nome
        self.idade = idade
        self.vida = vida
    
    def upgrade_vida(self):
        self.vida += 10

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'

p5 = Personagem('Samus', 30, 100)
print(p5.nome, p5.idade, p5.vida) # Samus 30 100
p5.upgrade_vida()
print(p5.vida) 

def imprimir_personagem(p):
    print(f'Nome: {p5.nome}, Idade: {p5.idade}, Vida: {p5.vida}')
    
