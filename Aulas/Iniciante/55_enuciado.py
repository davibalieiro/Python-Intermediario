n1 = input('Digite um numero inteiro: ')

if n1.isdigit():
    n2 = int(n1)
    decisao = n2 % 2 == 0
    opcao = 'impar'
    if decisao is True:
        opcao = 'par'
    print(f'O numero {n2} é {opcao}')

else:
    print('Voce nao digitou um numero inteiro')

horario = input('Digite a hora do dia: ')
print(horario)
if horario.isdigit():
    hora = int(horario)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Nao conheco essa hora')
else:
    print('Por favor, digite um numero inteiro')


nome = input('Digite seu primeiro nome: ')
print(f'Seu nome {nome}')
letras = len(nome)
if letras > 1:
    if letras <= 4:
        print('Seu nome é curto')
    elif letras >= 5 and letras <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Por favor digite mais de uma letra')
