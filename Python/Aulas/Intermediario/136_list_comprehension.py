# List comprehension em Python
# List comprehension - é uma forma rapida para criar lista a partir de iteraveis

import pprint


def p(v):
    pprint.pp(v, sort_dicts=False, width=40)


# print(list(range(10)))
# lista = []
# for n in range(10):

#    lista.append(n)

# print(lista)

# lista = [n for n in range(10)]
# print(lista)

# posso fazer com duas linhas kkkkkkk
# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'price': 20, },
    {'nome': 'p2', 'price': 10, },
    {'nome': 'p3', 'price': 30, },
]

# novo_produto = [
#    {**produto, 'price': produto['price']*1.05}
#    if produto['price'] > 20 else {**produto}
#    for produto in produtos
# ]

# print(*novo_produto, sep='\n')
# p(novo_produto)

lista = [n for n in range(10) if n < 5]
print(lista)

novo_produto = [
    {**produto, 'price': produto['price']*1.05}
    if produto['price'] > 20 else {**produto}
    for produto in produtos
    if (produto['price']*1.05) > 10
]

# List comprenshesion
# Isso é mais ou menos ultilizavel

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    (x, y) for x in range(3)
    for y in range(3)
]

print(lista)

# Dicionary Comprehension e Set Comprehension

product = {
    'name': 'Davi',
    'price': 2.5,
    'Categoria': 'Escritorio',

}

for chave, value in product.items():
    print(chave, value)

dicionario = {
    chave: value.upper()
    if isinstance(value, str) else value
    for chave, value
    in product.items()
    if chave != 'Categoria'

}
lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: value
    for chave, value in lista
}

# ou da pra fazer assim
# print(dict(lista))

print(dicionario)


# s1 = {i for i in range(10)}
print(set(range(10)))

# Dicionary Comprehension e Set Comprehension

product = {
    'name': 'Davi',
    'price': 2.5,
    'Categoria': 'Escritorio',

}

for chave, value in product.items():
    print(chave, value)

dicionario = {
    chave: value.upper()
    if isinstance(value, str) else value
    for chave, value
    in product.items()
    if chave != 'Categoria'

}

# dict compreshersion

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
dc = {
    chave: value
    for chave, value in lista
}

# ou da pra fazer assim
# print(dict(lista))

print(dicionario)


# s1 = {i for i in range(10)}
print(set(range(10)))
