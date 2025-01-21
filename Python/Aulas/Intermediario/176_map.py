# MAP - Para mapear dados

from functools import partial


def print_iterator(iterator):
    print(*list(iterator), sep='\n')
    print()


product = [
    {'nome': 'Produto 5', 'Preço': 10.00},
    {'nome': 'Produto 1', 'Preço': 22.32},
    {'nome': 'Produto 3', 'Preço': 10.11},
    {'nome': 'Produto 2', 'Preço': 105.87},
    {'nome': 'Produto 4', 'Preço': 69.90},
]


def porcetagem(v, p):
    return round(v*p, 2)


big_ten = partial(
    porcetagem, p=1.1
)


# novo_product = [
#     {**p, 'Preço': porcetagem(p['Preço'], 1.1)} for p in product
# ]
#  isso é uma func que aumenta o valor

def muda(product):
    return {**product, 'Preço': big_ten(product['Preço'])}


novo_product = map(
    muda, product
)

print_iterator(product)
print_iterator(novo_product)


# Na teoria isso vai dar certo, com o lambda se for uma def pequeno
# Serve para coisa grande com um mapeamento de dados

print(list(map(lambda x: x * 3, [1, 2, 3, 4])))
