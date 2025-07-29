# Aula de lista
'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indice e fatiamento
Metodos uteis: append, insert, pop, del, celar, extend, +
'''

#         012345
palavra = 'ABCDE'  # 5 caracteres len()
# lista = list() isso é isso:

#         0     1        2            3    4
lista = [123, True, 'Davi Balieiro', 1.2, []]
lista[2] = 'Cristiano'

print(lista[2])
print(lista)
# Aula de lista
'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indice e fatiamento
Metodos uteis: 
    append, insert, pop, del, celar, extend, +
    Create Read Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [1, 2, 3, 4]

lista[2] = 30

del lista[1]

print(lista)
print(lista[2])

lista.append(5)  # append() = ele adiciona um item ao final da lista
lista.pop()  # pop() = ele retira o ultimo item da minha lista
lista.append(6)
lista.append(7)
lista.pop()
print(lista)

# Aula de lista
'''
Lista em Python
Tipo list - Mutável
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indice e fatiamento
Metodos uteis: 
    append, insert, pop, del, celar, extend, +
    Create Read Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista = [1, 2, 3, 4]

lista[2] = 30

del lista[1]

print(lista)
print(lista[2])

lista.append(5)  # append() = ele adiciona um item ao final da lista
lista.pop()  # pop() = ele retira o ultimo item da minha lista
lista.append(6)
lista.append(7)
lista.pop()
print(lista)

'''
Cuidados com dados mutaveis
= - copiando o valor(imutaveis)
= - apnta para o mesmo valor na memoria

'''
lista_a = ['Davi', 'Cristiano', 1, True]
lista_b = lista_a.copy()


lista_a[0] = 'Suiiiii'

print(lista_a)
print(lista_b)

# Exiba os indices da lista
# Minha solução
lista = ['Davi', 'João', 'Augusto', 'Matheus', 'José']
i = -1
for nome in lista:
    print(i, '.', nome)
    i += 1

# Solução do Luíz
lista = ['Davi', 'João', 'Augusto', 'Matheus', 'José']
indeces = range(len(lista))

for i in indeces:
    print(i, lista[i])
