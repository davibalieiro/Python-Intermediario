# Class - classes sao moldes para criear novos objetos
# As classes geram novos objetos (inatcess) que podem ter seus 
# proprios atributos e metodos 
# Os Objetos gerados pelas classes podem usar seus dados internos 
# para realizar varias acoes
# Por convencao, usamos PascalCase para nomes de class

# name = 'Davi' #string
# print(name.upper())
# print(isinstance(name, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Davi', 'Balieiro')
# p1.nome = 'Davi'
# p1.sobrenome = 'Balieiro'
print(p1.nome)
print(p1.sobrenome)
