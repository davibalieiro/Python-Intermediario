# Class abstradas - ABC
# Uma classe abstrata é uma classe que não pode ser instanciada diretamente.
# @abstractmethod sao method que nao tem corpo 
# Metodos abstratos DEVEM ser implementados nas subclasses.
# É possivel criar @property @setter @classmethod @staticmethod @method como abstrata, para isso ue abstracmethod como decorator msais interno
# Foo - Bar -Baz são placeholders para nomes de classes, métodos ou atributos que você pode definir conforme necessário. 

from abc import ABC, abstractmethod

# EXEMPLO
# class Log(ABC):
#     @abstractmethod
#     def _log(self, msg):
#         ...

#     def log_error(self,msg):
#         return self._log(f'Error: {msg}')

#     def log_success(self,msg):
#         return self._log(f'Success: {msg}')

# class LogPrintMixin(Log):
#     def _log(self,msg):
#         msg_format = f'{msg} ({self.__class__.__name__})'
#         print(msg_format)

# l = LogPrintMixin()
# l.log_error('Any message')

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name
       
    @property
    @abstractmethod
    def name(self):
        return self._name
     
    @name.setter
    @abstractmethod
    def name(self, value):
        self._name = value

class Foo(AbstractFoo):

    def __init__(self, name):
        super().__init__(name)
        # print('I am Baka')

    @AbstractFoo.name.setter
    def name(self):
        return self._name

foo = Foo('Baz')
print(foo.name)