'''
Introdução as funções (def) em Python
Funções são trechos de codigo usados para
replicar determinada ação ao longo do seu codigo.
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, fuções em Python retornam None (Nada)

'''

'''
def Print(a, b, c):
    print('Suiii1')
    print('Suiii2')
    print('Suiii3')
    print('Suiii4')
'''

'''
def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)
imprimir(4, 5, 6)
'''


def ola(nome='Sem nome'):
    print(f'Olá {nome}')


ola('Musarelo')
ola('Jorge')
ola('Heleno')
ola()
