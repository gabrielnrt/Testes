# Esse é primeiro teste tentando usar classes em python

class Jogador:
    def __init__(self, nome, idade, rating):
        self.nome = nome
        self.idade = idade
        self.rating = rating

a = Jogador('Kasparov', 68, 2800)

print(a.rating)
