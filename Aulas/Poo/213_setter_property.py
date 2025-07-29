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
        if value == 'Red':
            raise ValueError('Color not allowed')
        self._color = value

car = Car('Blue')
car.color = 'Red'
