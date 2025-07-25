# Relacoes entre class: Associacao, Agregacao e Composisao
# Associacao é um tipo de relacao onde os objetos estao ligados dentro do sistema
# Agregacao é um tipo de relacao onde um objeto é composto por outros objetos
# Composisao é um tipo de relacao onde um objeto é composto por outros objetos e a existencia do objeto composto depende do objeto que o compoe
# Geralmente, temos uma associacao quajndo um objeto tem um atributo que refencia outro objeto

# Codigo Exemplo

'''
class Car:
    def __init__(self, name):
        self.nome = name
        self._person = None

    @property
    def person(self):
        return self._person
    
    @person.setter
    def person(self, person):
        self._person = person

class Person:
    def __init__(self, name):
        self.nome = name

    def name_person_car(self):
        return f'{self.nome} esta digirindo o carro '

car = Car('Mustang')
person_name = Person('José')
car.person = person_name

print(person_name.name_person_car())
'''

# Exemplo de Agregacion


'''
class Car:
    def __init__(self):
        self._product = []

    def sale(self):
        return sum([p.price for p in self._product])
    
    def insert_product(self, *product):
        for products in product:
            self._product.append(products)

    def list_product(self):
        print()
        for product in self._product:
            print(product.name, product.price)

class Product:
    def __init__(self, name, price):
        self.nome = name
        self.preco = price

car = Car()
p1, p2 = Product('Apple', 2.29), Product('Kiwi', 3.98)
car.insert_product(p1, p2)
car.insert_product()
print(car.sale())
'''

# Exemplo de Composicao

class Car:
    def __init__(self, name,):
        self.nome = name
        self.product = []
    
    def insert_product(self, value, number):
        self.product.append(Product(value, number))

    def list_car(self,):
        for cars in self.product:
            return f'{cars.value} e {cars.number}'

class Product:
    def __init__(self, value, number):
        self.value_person = value
        self.number_person = number

    def __del__(self):
        print('Apagando', self.value_person, self.number_person)


car = Car('Mustang')
car.insert_product('ABC', 78.9)
print(car)
print('#' * 40)
print(car.list_car())
