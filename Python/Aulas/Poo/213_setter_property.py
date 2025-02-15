# @property - um getter no modo python
# getter - metodo para obter um atributo
# Geralmente é usada nas seguintes situações:
# com getter
# p/ evitar quebrar codigo cliente
# p/ habilitar getter
# p/ executar ações ao obter um atributo
# Codigo cliente - é o codigo que usa seu codigo
# Atributos que comcecam com _ ou __ são priv

class Car:
    def __init__(self, color):
        # private protected 
        self._color = self.color

    @property
    def color(self):
        print('Property my Color')
        return self.color

    @color.setter
    def color(self, value):
        print('Set my Color')
        self._color = value

    
def ver_car(car):
    return car.color


car = Car('Blue')
# car.color = 'Red'

# getter -> obter valor
ver_car(car)