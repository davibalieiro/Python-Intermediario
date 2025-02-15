# @staticmethod sao inuteis em Python
# Metodo estatico sao que estao dentro 
# da class mas nao tem acesso ao self

class Pessoa: 
    @staticmethod
    def funaco(*args, **kwargs):
        print('Oi', args, kwargs)

def abu(*args, **kwargs):
    print()

c1 = Pessoa()
c1.funaco(1,2,3)
abu(1,2,3)
Pessoa.funaco(nomeado=1)
abu(nomeado=1)
