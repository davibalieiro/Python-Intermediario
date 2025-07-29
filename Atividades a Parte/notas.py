"""
Escreva um programa que peça ao usuário para inserir as notas 
de um aluno (valores entre 0 e 10). O programa deve continuar pedindo 
notas até que a qtd de notas seja 10 
Em seguida, o programa deve calcular e exibir a média das notas inseridas.
"""

# nota de aluno 0 - 10
notas_lista = []
while True:

    try:
        notas = float(input('Digite a nota: '))  # <-- ATÉ 10 indice
        if notas > 10:
            print('Apenas notas validas (0 - 10)')
        elif notas < 10 and notas > 0:
            notas_lista.append(notas)
            print('Valor adicionado')
    except:
        print('Error')

    if len(notas_lista) == 10:
        for i in notas_lista:
            multiplicarnumeros = i * i
            res = multiplicarnumeros / 10

        print(f'Média: {res}')

        break
