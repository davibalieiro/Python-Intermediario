import sys

# Generator expression, Iterable e Iterators em Python

iterable = ['Eu', 'Tenho', '__iter__']
iterador = iterable.__iter__()  # tem__iter__e__next__
print(next(iterador))

# O Iterador não sabe nada, ele so sabe te entregar o proximo valor

lista = [n for n in range(1000000)]
gerenator = (n for n in range(1000000))
print(sys.getsizeof(lista))
print(sys.getsizeof(gerenator))

for n in gerenator:
    print(n)

# Introdução as Gernerator function em Python
# generator = (n for n in range(1000000))

# def generator(n=0): # Todo def que tem yield é um generator
#     yield 1  # Pausar
#     print('Boraaa...')
#     yield 2 # Pausar
#     print('...')
#     yield 3 # Pausar
#     print('Ultimo')
#     return 'Acabou' # Só vai executar se alcançar StopIteration

# gen = generator(n=0)
# for n in gen:
# print(n)
def generator(n=0, maximum=10):  # Todo def que tem yield é um generator
    while True:
        yield n
        n += 1

        if n > maximum:
            return


gen = generator(n=1, maximum=100)
for n in gen:
    print(n)

# Yield from


def gen1():
    yield 1
    yield 2
    yield 3
    return 'Acabo'


def gen3():
    yield 10
    yield 20
    yield 30
    return 'Acabo'


def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6
    return 'Acabo'


genfuntion = gen2(gen1)
genfuntion2 = gen2(gen3)

for n in genfuntion:
    print(n)

for n in genfuntion2:
    print(n)
