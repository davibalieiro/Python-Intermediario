# Iterando strings co while
'''
nome = 'Davi Balieiro'
tam_nome = len(nome)
print(nome)
print(tam_nome)

nova_string += "*D*"
'''
nome = 'Cristiano Ronaldo'
n1 = 0
novo = ''
while n1 < len(nome):
    letra = (nome[n1])
    novo += f'*{letra}'
    n1 += 1
novo += f'*'
print(novo)


# Calculadora com While
while True:

    n1 = input('Digite o primeiro numero: ')
    n2 = input('Digite o segundo numero: ')
    operador = input('Digite o operador desejado = + - * /\n')

    numeros_val = None
    nu1 = 0
    nu2 = 0
    try:
        nu1 = float(n1)
        nu2 = float(n2)
        numeros_val = True

    except:
        numeros_val = None

    if numeros_val is None:
        print('Um numero digitado nao é valido')
        continue

    operador_val = '+-*/'
    if operador not in operador_val:
        print('Um operador digitado nao é valido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Seu resulatado é esse confira a baixo:\n')
    if operador == '+':
        print(nu1 + nu2)
    elif operador == '-':
        print(nu1 - nu2)
    elif operador == '*':
        print(nu1 * nu2)
    elif operador == '/':
        print(nu1 / nu2)

    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    if sair:
        break


# Calculadora com While
while True:

    n1 = input('Digite o primeiro numero: ')
    n2 = input('Digite o segundo numero: ')
    operador = input('Digite o operador desejado = + - * /\n')

    numeros_val = None
    nu1 = 0
    nu2 = 0
    try:
        nu1 = float(n1)
        nu2 = float(n2)
        numeros_val = True

    except:
        numeros_val = None

    if numeros_val is None:
        print('Um numero digitado nao é valido')
        continue

    operador_val = '+-*/'
    if operador not in operador_val:
        print('Um operador digitado nao é valido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Seu resulatado é esse confira a baixo:\n')
    if operador == '+':
        print(nu1 + nu2)
    elif operador == '-':
        print(nu1 - nu2)
    elif operador == '*':
        print(nu1 * nu2)
    elif operador == '/':
        print(nu1 / nu2)

    sair = input('Quer sair? [s]sim: ').lower().startswith('s')
    if sair:
        break
