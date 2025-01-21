primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

# Aula de AND
# and/ or/ not
#   e/ ou/ não
# and = Todas as afirmações precisam ser verdadeiras
# None é usado para representar um não valor
entrada = input('E = entrar ou S = sair:')
print(entrada)
senha = input('Senha: ')

valor_senha = '1234'
# if condição == True
if entrada == 'E' and senha == valor_senha:
    print('Entrar')

else:
    print('Sair')

print(True and False and True)

# Aula de OR
# Or = Uma expressão verdadeira = tudo verdadeiro
entrada = input('E = entrar ou S = sair:')
print(entrada)
senha = input('Senha: ')

valor_senha = '1234'
# if condição == True
if (entrada == 'E' or entrada == 'e') and senha == valor_senha:
    print('Entrar')

else:
    print('Sair')

# Alaviação de curto circuito
# print(True and False and True)
senha = input('Senha: ') or 'Sem senha'
print(senha)

# Aula de NOT
# Not = Usado para inverter expressões
# not True = False
# not False = True
print(not False)

# Aula de in e in not
# Strings são iteráveis
#  0 1 2 3
#  D A V I
# -4-3-2-1

nome = 'Davi'
# print(nome[3])
print('D' in nome)
print('F' in nome)
print(10 * '-')
print('D' not in nome)
print('F' not in nome)


pessoa = input('Digite seu nome: ')
buscar = input('O que deseja buscar: ')

if buscar in nome:
    print(f'{buscar} esta em {nome}')

else:
    print(f'{buscar} não esta em {nome}')
