# Herança simples  - Relação entre classes
# Associação - usa 
# Agregação - tem
# Composição - é dono de
# Herança - é um

# object - class base, super class, parent class - ela ja é object
class Person:
    any = '12345'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    def seapk_name_class(self):
        print(self.name,"=",self.__class__.__name__)

class Customer(Person):
        def seapk_name_class(self):
            print("Customer")
            print(self.name,"=",self.__class__.__name__)

class Student(Person):
    print("Student")
    any = '54321'

c1 = Customer('João', 'Silva')
c1.seapk_name_class()
s1 = Student('Maria', 'Oliveira')
s1.seapk_name_class()
print(c1.any)
print(s1.any)
