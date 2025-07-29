# Funções decaradoras
# Decorar = Adicionar Remover Restringir Alterar
# São funções que decorar outras funções
# Usar em Python
# O Python tem um açucar Sintatico @sytax_sugar


def criar(funcao):
    def interna(*args, **kargs):
        for i in args:
            e_string(i)
        resultado = funcao(*args, **kargs)
        return resultado

    return interna


@criar
def inverter(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Paramentro deve ser srtings')


inverter_chegando = criar(inverter)


inver = inverter('Davi')
print(inver)

def fabrica_de_decoradores(a=None, b=None, c=None):
    def decoradora(func):
        print('Decoradora 1')

        def anilhada(*args, **Kwargs):
            print('Aninhadas')
            res = func(*args, **Kwargs)
            return res
        return anilhada
    return decoradora


mult = fabrica_de_decoradores()(lambda x, y: x*y)


@fabrica_de_decoradores()
def soma(x, y):
    return x + y


valor = soma(5, 10)
print(valor)
print(mult)


def parametros_decorador(name):
    def decorador(func):
        print('trem')

        def sua_new_func(*args, **Kwargs):
            res = func(*args, **Kwargs)
            final = f'{res} {name}'
            return final
        return sua_new_func
    return decorador


@parametros_decorador(name='Suiii')
def soma(x, y):
    return x+y


valor = soma(10, 5)
print(valor)
