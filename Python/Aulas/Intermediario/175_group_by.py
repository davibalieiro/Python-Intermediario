# GROUP BY = Agrupamento de valores (MySQL) (Itertools)

from itertools import groupby

alunos = [
    {'nome': 'jao0', 'nota': 'A'},
    {'nome': 'jao1', 'nota': 'B'},
    {'nome': 'jao2', 'nota': 'A'},
    {'nome': 'jao3', 'nota': 'C'},
    {'nome': 'jao4', 'nota': 'D'},
    {'nome': 'jao5', 'nota': 'A'},
    {'nome': 'jao6', 'nota': 'B'},
    {'nome': 'jao7', 'nota': 'A'},
    {'nome': 'jao8', 'nota': 'C'},
    {'nome': 'jao9', 'nota': 'B'}
]


def ordena(aluno):
    return aluno['nota']


alunos_gruop = sorted(alunos, key=ordena)

# alunos = ['a', 'b', 'c']
grupos = groupby(alunos_gruop, key=ordena)
for chave, i in grupos:
    print(chave)
    for aluno in i:
        print(aluno)
