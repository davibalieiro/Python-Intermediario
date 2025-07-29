# Lista de listas

salas = [
    ['Mario', 'Joana'],  # 0
    ['Heleno'],  # 1
    ['Musarelo', 'Cristiana', 'Elizabetho',]  # 2
    # ['Musarelo', 'Cristiana', 'Elizabetho', (0, 10, 20, 30, 40)]  # 2
]
print(salas[0][1])
print(salas[1][0])
print(salas[2][2])
print(salas[2][3][2])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
