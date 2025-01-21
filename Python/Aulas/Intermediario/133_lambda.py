'''
Função lambda em Python
A função lambda é uma funçao como qualquer outra em python
Porém, são funções anõnimas que cotem apenas uma linha
Ou seja tudo deve ser contido dentro de uma unica expressão
lista = [
    {'nome': 'Luiz','sobrenome': 'Otavio'},
    {'nome': 'Luiz','sobrenome': 'Otavio'},
    {'nome': 'Luiz','sobrenome': 'Otavio'},
    {'nome': 'Luiz','sobrenome': 'Otavio'},
    {'nome': 'Luiz','sobrenome': 'Otavio'},
]
'''

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Otavio'},
    {'nome': 'Davi', 'sobrenome': 'Otavio'},
    {'nome': 'Maria', 'sobrenome': 'Otavio'},
    {'nome': 'Gustavo', 'sobrenome': 'Otavio'},
    {'nome': 'Eulla', 'sobrenome': 'Otavio'},
]


def exibir(lista):
    for item in lista:
        print(item)


lista.sort(key=lambda item: item['nome'])
print(lista)
