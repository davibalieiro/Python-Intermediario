# Herança simples  - Relação entre classes
# Associação - usa 
# Agregação - tem
# Composição - é dono de
# Herança - é um

# object - class base, super class, parent class - ela ja é object
# class Person:
#     any = '12345'
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
    
#     def seapk_name_class(self):
#         print(self.name,"=",self.__class__.__name__)

# class Customer(Person):
#         def seapk_name_class(self):
#             print("Customer")
#             print(self.name,"=",self.__class__.__name__)

# class Student(Person):
#     print("Student")
#     any = '54321'

# c1 = Customer('João', 'Silva')
# c1.seapk_name_class()
# s1 = Student('Maria', 'Oliveira')
# s1.seapk_name_class()
# print(c1.any)
# print(s1.any)

# # super() 
# class MyStr(str):
#     def upper(self):
#         print('Antes')
#         return super().upper()


# any = MyStr('Davi')
# print(any.upper())

class A:
    attribute_a = 'a1'

    def __init__(self, attribute):
        self.attribute = attribute

    def a(self):
        print('a')

class B(A):
    attribute_b = 'b1'
    def a(self):
        print('b')

    def __init__(self, attribute, any):
        super().__init__(attribute)
        self.any = any

class C(B):
    attribute_c = 'c1'
    def a(self):
        # super(C, self).a()
        # super(B, self).a()
        # super(A, self).a()
        print('c')
    
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Burlei, os Abus')

# print(A.mro())
# print(B.mro())
# print(C.mro())
c = C('Abu','Abu1')
print(c.attribute)
print(c.any)
# print(c.attribute_a)
# print(c.attribute_b)
# print(c.attribute_c)
c.a()