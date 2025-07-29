# Metodos de class + factories
# sao metodos onde self sera cls ou seja
# ao inves de receber a isinstance no primeiro
# paramentro receberemos a propria class

class Pessoa:
    ano = 2025 # atributo de class

    def __init__(self, name, years) -> None:
        self.nome = name
        self.idade = years

    @classmethod
    def metodo(cls):
        print('Hey')

    @classmethod
    def pai_50(cls, name):
        return cls(name, 50)
    
    @classmethod
    def anom(cls, idade):
        return cls('Anomima', idade)

p1 = Pessoa('Cr7', 40)
p2 = Pessoa.pai_50('Davi')
p3 = Pessoa.anom(20)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# print(Pessoa.ano)
# Pessoa.metodo(p1)
