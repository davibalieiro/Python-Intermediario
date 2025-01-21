# Aula com Exercicios de Funções

'''
1-) Crie uma função em multiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel. 
'''

'''
2-) Crie uma função que fala se um numero é par ou impar
Retorne se o numero é par ou impar.
'''

# 1-)


def mult(*agrs):
    total = 0
    for i in agrs:
        total += i
        return total


resultado = mult(1*2*3*4*5)
print(f'1-) {resultado}')


# 2-)

def coisar(a):
    if a != 0:
        print(f'2-) {a} é impar')
    else:
        print(f'2-) {a} é par')
        return a


coisar(3)
