"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

lista = []
while True:

    print('Selecione uma opção\n')

    opcao = input('[i] Inserir [a] Apagar [l] Listar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        indice = input('Escolha uma opção: ')

        try:
            indices = int(indice)
            del lista[indices]

        except:
            print('Não foi possivel apagar')

    if opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')

        i = 0
        for valor in lista:
            print(i, '.', valor)
            i += 1
        else:
            print('Digite alguma coisa valida')
