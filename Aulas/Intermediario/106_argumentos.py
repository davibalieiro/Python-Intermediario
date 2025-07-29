'''
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual 
Argumentos não nomeados recebe apenas o argumento (valor)

'''


def soma(x, y, z):
    # Definição
    print(f'{x=} {y=} {z=}', '|' 'x + y + z =', x + y + z)


soma(1, 2, 3)
soma(y=2, z=1, x=3)  # Apatir do momento que passar um argumento para o paramento os outros tambem devem receber argumentos (exemplo: soma(1, y=2, z=3))

print(1, 2, 3, sep='-')
