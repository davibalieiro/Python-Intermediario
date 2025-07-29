# @property - um getter no modo python
# getter - metodo para obter um atributo
# Geralmente é usada nas seguintes situações:
# com getter
# p/ evitar quebrar codigo cliente
# p/ habilitar getter
# p/ executar ações ao obter um atributo
# Codigo cliente - é o codigo que usa seu codigo
'''
class Car:
    def __init__(self, color):
        # private protected public

        self.color = color

    def getter_color(self):
        print('Get Color')
        return self.color
    

car = Car('Blue')
# print(car.color)
print(car.getter_color())
'''

class Car:
    def __init__(self, color):
        # private protected public
        self.color_init = color

    @property
    def color(self):
        print('Property')
        return self.color_init

    @property
    def color_cap(self):
        print('Color_cap')
        return 1,2,3

car = Car('Blue')
print(car.color)