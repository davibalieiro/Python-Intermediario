# Aula de Repetição
# while (enquanto)
# Executa uma ação enquanto uma condiçãofor verdadeira

valor = True
while valor:
    nome = input('Qual o seu nome ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break
print('Acabou')

# Aula de Repetição
# while (enquanto)
# Executa uma ação enquanto uma condiçãofor verdadeira
# # Aula sobre contador = contador + 1 ou x=x+1
'''
Operadores de atribuição 
= += -= *= /= //= **= %=
'''
contador = 0
while contador <= 10:
    print(contador)
    contador = contador + 1
print('Acabou')

i = 0
# Isso é igual a =
i += 1

# Aula de while
# loop infinito = Quando o codigo nao tem fim

i = 1
while i <= 100:
    i += 1
    print(i)
    if i == 10:
        print('Nao vou mostra o 10')
        continue
    if i >= 11 and i <= 30:
        #        print('Nao vou mostra do ',i)
        continue

    if i == 50:
        break
print('Acabou')

linhas = 3
colunas = 3

linha = 1
coluna2 = 1
while linha <= linhas:
    coluna2 = 1
    while coluna2 <= colunas:
        print(f'{linha=} {coluna2=}')
        coluna2 += 1
    linha += 1


print('Acabou')
