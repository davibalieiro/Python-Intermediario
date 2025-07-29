# Atributo de class

class Pessoa:
    years_atual = 2025
    def __init__(self, name, years) -> None:

        self.nome = name
        self.idade = years
    
    def get_years(self):
        return self.years_atual - self.idade

p1 = Pessoa('cr7', 40)
p2 = Pessoa('cr7', 22)
print(p1.get_years())
print(p2.get_years())