# Encapsulamento (modificadores de acesso: public, protected, private)
# Python Não tem modificadores de acesso
# Mas podemos seguir as seguintes convenções 
#     (sem underline) = pubic
#         pode ser usado em qualquer lugar
#     (um _ ) = protected
#         não deve ser usado fora da class
#     (dois __ ) = private
#         só deve ser USADO e class que ja foi declarada

class Foo:
    def __init__(self):
        self.__attr = 'Atributo privado'
        self._attr = 'Atributo protegido'
        self.attr = 'Atributo publico'

    def method_public(self):
        self.__method_private()
        return 'Metodo publico'

    def _method_protected(self):
        print(self.__attr)
        return 'Metodo protegido'

    def __method_private(self):
        return 'Metodo privado'

f = Foo()
# print(f.attr)
# print(f.method_public())