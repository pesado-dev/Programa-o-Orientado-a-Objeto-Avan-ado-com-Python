class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir(self):
        print(self.nome, self.idade)
p = pessoa('Marcio', 35)
