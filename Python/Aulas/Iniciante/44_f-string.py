'''
Interpolaração basica de strings
s - strings
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
'''
nome = 'Davi'
preco = 100.89769
valores = '%s, o preço é R$%.2f' % (nome, preco)
print(valores)
print('O hexadecimal de %d é %x' % (15, 15))

'''
Interpolaração basica de strings
s - strings
d - int
f - float
.<numero de digitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
'''
valor = 'Suii'
print(f'{valor}')
print(f'{valor: <10}')
print(f'{valor: >10}')
print(f'{valor: ^10}')
print(f'{1000.9897835:.3f}')

'''
Fateamento de Strings
 012345678
 Olá mundo
-987654321
Fateamento [i:f:p] [::]
Obs: a funcao len retorna a quant
de caracteres da str
'''
valor = 'Olá mundo'
print(valor[0:3])
print(len(valor))
# print(valor[0:9:1])
print(valor[-1:-10:-1])

nome = input('Digite seu nome: ')
idade = input('Digite seu idade: ')
if nome and idade:
    print(f'Você tem {idade} de idade')
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido fica {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome nao contém espaços')
    # nome_len = len(nome)
    # print(f'Seu nome tem {nome_len} letras')
    print(f'Seu tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')

else:
    print('Desculpa, você é uma mula e nao degitou nada')
