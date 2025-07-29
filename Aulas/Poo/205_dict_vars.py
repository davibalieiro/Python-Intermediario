# Atributo de class

class Pessoa:
    years_atual = 2025
    def __init__(self, name, years) -> None:

        self.nome = name
        self.idade = years
    
    def get_years(self):
        return self.years_atual - self.idade

p1 = Pessoa('cr7', 40)
p1.nome = 'abu'
print(p1.__dict__)
print(vars(p1))