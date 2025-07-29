# Herança multipla - é um tipo de herança onde uma classe pode herdar de mais de uma classe base.
class A:
    ...
    
    def speak(self):
        print('a')
class B(A):
    ...

    def speak(self):
        print('b')

class C(A):
    ...

    def speak(self):
        print('c')
    
class D(B,C):
    ...
    def speak(self):
        print('d')

d = D()
d.speak()
print(D.mro()) # method class
# print(D.__mro__) # pode ser usado assim 