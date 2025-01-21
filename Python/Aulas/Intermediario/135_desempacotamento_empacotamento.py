# Aula de Desempacotamento e Empacotamento de Dicionarios
a, b = 1, 2
a, b = a, b

print(a, b)

pessoa = {
    'nome': 'Davi',
    'sobrenome': 'Balieiro',
}

dados = {
    'idade': 17,
    'altura': 1.87,
}

pessoa_completa = {**pessoa, **dados}
# print(pessoa_completa)


def mostar(*arges, **karges):
    print('Não nomeados:' , arges)

    for chave,valor in karges.items():
        print(chave,valor)


mostar(nome='Davi', idades=12)


# IMPORTANTE
(a1, a2), (b1, b2) = pessoa.values()
print(a1, a2)
print(b1, b2)

for item, valor in pessoa.items():
    print(item, valor)
