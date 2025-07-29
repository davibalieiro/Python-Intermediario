# Exercicio - Objetivo - Unir listas
# Crie uma func zipper(Como o zipper de roupa)
# O trabalho dessa func sera unir duas lista em ordem
# Use todos os valores da menor lista
# Ex:
# ['Salvador', 'Ubatuba', 'Belo Horizonte'],
# ['BA', 'SP', 'MG', 'RJ']
# resultado:
# [('Salvador', 'BA'),('Ubatuba', 'SP'),('Belo Horizonte', 'MG')]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte'],
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1, l2)))
