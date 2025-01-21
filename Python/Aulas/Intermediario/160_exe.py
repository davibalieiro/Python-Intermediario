# Exercicios

import copy
product = [
    {'nome': 'Produto 5', 'Preço': 10.00},
    {'nome': 'Produto 1', 'Preço': 22.32},
    {'nome': 'Produto 3', 'Preço': 10.11},
    {'nome': 'Produto 2', 'Preço': 105.87},
    {'nome': 'Produto 4', 'Preço': 69.90},
]
new_product = [
    {**i, 'Preço': round(i['Preço'] * 1.1, 2)}
    for i in copy.deepcopy(product)

]

product_new = sorted(product,
                     key=lambda p: p['nome'],
                     reverse=True
                     )

print(product, sep='\n')
print()
print(product_new)

product_new_preco = sorted(product,
                           key=lambda p: p['Preço'],
                           )

print()
print(product_new_preco)
