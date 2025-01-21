# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
    'idade': 17,
    'altura': 1.9,
    'endereços': [
         {'rua': 'suiiiii', 'número': 570},
         {'rua': 'outra rua', 'número': 989},
    ]
}

# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

print(pessoa['nome'])
print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])

# Manipulado chaves e valores em dicionarios

pessoa = {}


chave = 'nome'
pessoa[chave] = 'Davi Balieiro'
pessoa['sobrenome'] = 'Costa'

del pessoa['sobrenome']

print(pessoa)

print(pessoa['nome'])

if pessoa.get('sobrenome', None):  # .get() - tenta obter uma chave, padrao None
    print('existe')

# Metodos uteis dos dicionarios em Python
'''
len - quantas chaves
keys - iteravel com as chaves
values - iteravel com o valores
items - iteravel com o valores e as chaves
setdefaut - adiciona valor se a chave nao existe
copy - retorna uma copia rasa (shallow copy)
get - obtem uma chave
pop - apaga um item com a chaves especifica (del)
popitem - Apaga o ultimo item adicionado
update - Atualiza um dicionario com o outro

'''

import copy
# import copy - isso é uma copy profunda ou seja um dicionario nao vai afetar o outro, provavel que vou utilizar muito em lista
# .copy - é uma copy mais rasa so o basico

pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
    'idade': 900,
}

pessoa.setdefault('idade', None)
print(pessoa['idade'])

# print(pessoa.__len__()) mesma coisa que isso
print(len(pessoa))

print(list(pessoa.keys()))

print(list(pessoa.values()))

print(list(pessoa.items()))


for chaves in pessoa.values():
    print(chaves)


for chaves, valor in pessoa.items():
    print(chaves, valor)

# .update - é para atualizar uma lista ou adicionar algo nela mesma
'''
pessoa.update({
    'nome': 'Cr7',
})
'''

pessoa.update(nome='Junior,', idade=90)
print(pessoa)
