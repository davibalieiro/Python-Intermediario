'''
Operação Ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
'''
# print('Valor' if True else 'Outro valor')
# print('Valor' if False else 'Outro valor')

condicao = 10 == 10
valor = 'Valor' if condicao else 'Outro valor'
print(valor)

digito = 9
novo = digito if digito <= 9 else 0
print(novo)
