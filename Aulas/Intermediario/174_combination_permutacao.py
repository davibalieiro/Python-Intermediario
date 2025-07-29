# Combination, Permutation e Product - Itertools
# Combinacao - Ordem nao importa - iteravel - tamanho do grupo
# Permutacao - Ordem Importa
# Produto - Ordem importa e repete valores unico

# from itertools import combinations, permutations, product PODE SALVAR MUITO NA HORA DE ORDERNAR.
from itertools import combinations, permutations, product


def print_iterator(iterator):
    print(*list(iterator), sep='\n')


pessoa = [
    'joao', 'joana', 'luiz', 'leticia'
]

camisa = [
    ['Preta', 'Branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino', 'Unisex'],
    ['Algodao', 'Poliester']
]

print_iterator(combinations(pessoa, 2))
print_iterator(permutations(pessoa, 2))
print_iterator(product(*camisa))
