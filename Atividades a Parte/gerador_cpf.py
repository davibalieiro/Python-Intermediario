import random
for _ in range(10):
    digitos_pessoa = ''
    for i in range(9):
        digitos_pessoa += str((random.randint(0, 9)))

    i = 10

    resultado_1 = 0
    for numero in digitos_pessoa:
        resultado_1 += int(numero) * i
        i -= 1
    digito_1 = ((resultado_1 * 10) % 11)
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # Esse é o calculo do outro digito
    digitos_pessoa_2 = digitos_pessoa + str(digito_1)
    i = 11

    resultado_2 = 0
    for numero_2 in digitos_pessoa_2:
        resultado_2 += int(numero_2) * i
        i -= 1
    digito_2 = ((resultado_2 * 10) % 11)
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_calculado = f'{digitos_pessoa}{digito_1}{digito_2}'

    print(cpf_calculado)
