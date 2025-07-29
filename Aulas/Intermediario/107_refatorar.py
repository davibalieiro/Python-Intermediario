'''
Valores padrão para parametros
Ao definir uma função, os parametros podem 
ter valores padrão. Caso o valor não seja enviado
para o parametro, o valor padrão será usado.

Refatorar: editar o seu codigo.

'''


def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=} ', x + y)


soma(1, 2)
soma(2, 5)
soma(40, 60)
soma(y=20, x=60, z=0)
