# filter é um filtro funcional
def iter(iterador):
    print(*list(iterador), sep='\n')
    print()


product = [
    {'nome': 'Produto 5', 'Preço': 10.00},
    {'nome': 'Produto 1', 'Preço': 22.32},
    {'nome': 'Produto 3', 'Preço': 10.11},
    {'nome': 'Produto 2', 'Preço': 105.87},
    {'nome': 'Produto 4', 'Preço': 69.90},
]

# new_product = [
#     p for p in product
#     if p['Preço'] > 20
# ]

new_product = filter(
    lambda p: p['Preço'] > 20, product
)

iter(product)
iter(new_product)

