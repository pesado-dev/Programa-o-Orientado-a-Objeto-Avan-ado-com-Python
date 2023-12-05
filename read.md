class pessoa:
#atributo = variável
    nome = 'marcio'
    idade = 35
#metodo = função
def exibir(self, nome, idade):
    print(nome, idade)
#use o valor da própria classe
#use o valor desta mesma classe
#this(outras linguagens), python `self`

def __init__(self,nome,idade):
    self.nome=nome
    self.idade=idade
    print(self.nome,self.idade)

arquivo 2
#from pessoa import `pessoa`
#p = pessoa()
#p.exibir()

from pessoa import pessoa
Pessoa = pessoa('Marcio',35)
#pessoa1 = pessoa()
#print(pessoa.nome)
#print(pessoa.idade)
#Pessoa.exibir('marcio',38)
#pessoa1.exibir('benedito',22)   