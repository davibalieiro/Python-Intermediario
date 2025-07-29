# Reduce - faz a reducao de um iteravel em um valor
from functools import reduce

product = [
    {'nome': 'Produto 5', 'Preço': 10.00},
    {'nome': 'Produto 1', 'Preço': 22.32},
    {'nome': 'Produto 3', 'Preço': 10.11},
    {'nome': 'Produto 2', 'Preço': 105.87},
    {'nome': 'Produto 4', 'Preço': 69.90},
]

# total = 0 
# for n in product:
#     total += n['Preço']

# print(total)

def func_reduce(prev,param):
    print(prev)
    print('product',product)
    return prev + param['Preço']


total = reduce(
    func_reduce,
    product,
    0
)