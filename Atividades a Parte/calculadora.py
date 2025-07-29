while True:
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    operador = input('Digite o operador matematico (+-*/):\n')
    nu1 = 0
    nu2 = 0

    nu1 = float(n1)
    nu2 = float(n2)
    if operador == '+':
        print(nu1 + nu2)
    elif operador == '-':
        print(nu1 - nu2)
    elif operador == '*':
        print(nu1 * nu2)
    elif operador == '/':
        print(nu1 / nu2)
    sair = input('Deseja sair [s]sim: ').startswith('s')
    if sair:
        break
print('Resulado determinado, operação concluida')
