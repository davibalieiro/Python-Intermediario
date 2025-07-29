while True:
    try:
        entrada = int(input('Digite um numerinho: '))
        if entrada <= 0:
            print('Digite um numero inteiro positivo')
            continue
    except:
        print('Erro')
        continue

    resultado = entrada
    print(f'Os numeros foram: ')
    counter = 1
    while resultado != 1:

        print(f'{counter} | {resultado}')

        if resultado % 2 == 0:
            resultado = resultado // 2

        else:
            resultado = resultado * 3 + 1

        counter += 1

    print(f'{counter} | {resultado}')
