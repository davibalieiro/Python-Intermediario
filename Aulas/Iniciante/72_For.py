# Aula de For/in = "para"
# O while é pra quando nao sei quantas vezes o repetir
# For eu sei
'''
texto = 'Python'
i = 0
tamanho = len(texto)
while i < tamanho:
    print(texto[i])
    i += 1
'''
'''
senha = '1234'
senha_digitada = ''
i = 0
while senha != senha_digitada:
    senha_digitada = input(f'Digite a senha({i})x: ')
    i += 1
print(i)
print('Acabou aqui')
'''
texto = 'Python'
ntexto = ''
for letra in texto:
    ntexto += f'*{letra}'
    print(letra)
print(f'{ntexto}*')

'''
For + range
range = range(start, stop, step)
'''
# numeros = range(10)
numeros = range(0, 8, 8)

for valor in numeros:
    print(valor)

    # Dica: da pra fazer a tabuada com isso
'''
numeros = range(0, 81, 8)
i = 0
for valor in numeros:

    print(f'{i} x 8 = {valor}')
    i += 1
'''
'''
Iterável = str, range ,etc (__iter__)
Iterador = quem sabe entregar um valor de cada vez
next = me entrague o proximo valor
iter = me entrague seu iterador
'''
'''
nome = 'Davi'.__iter__()
nome = iter('Davi')
print(next(nome))
print(nome.__next__())
'''
# Tudo isso é o que o FOR faz por "debaixo dos panos"
'''
nome = 'Davi'
iterator = iter(nome)

while True:

    try:
        print(next(iterator))

    except StopIteration:
        break
'''

# TUDO ISSO É IGUAL A = ISSO:
nome = 'Davi'
for letra in nome:
    print(letra)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    if i == 5:
        print('i é 5, pulando...')
        continue


    if i == 8:
        print('i é 8, seu else nao existe')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For sussec')
