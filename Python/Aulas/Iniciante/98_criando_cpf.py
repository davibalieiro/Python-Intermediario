
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)


# cpf_recebido = '74682489070'\
#    .replace('.','')\
#    .replace(' ','')\
#    .replace('-','')

# Isso é igual a isso:
import re
import sys
import random
cpf = input('Digite seu CPF: ')
cpf_recebido = re.sub(
    r'[^0-9]', '', cpf
)

primeiro_carater_repetido = cpf == cpf[0] * len(cpf)
if primeiro_carater_repetido:
    print('Sua mula é pra digitar o seu CPF')
    sys.exit()

digitos_pessoa = cpf_recebido[:9]
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

cpf_calculado = f'{resultado_1}{digito_1}{digito_2}'

if cpf_recebido == cpf_calculado:
    print(f'{cpf_recebido} é valido')
else:
    print(f'{cpf_recebido} não é valido')


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

cpf_calculado = f'{resultado_1}{digito_1}{digito_2}'

print(cpf_calculado)
