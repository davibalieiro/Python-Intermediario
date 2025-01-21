# Exercicio - Sistema de Pergunta e Resposta

pergunta = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opcões': ['1', '3', '4', '5'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcões': ['20', '10', '25', '50'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcões': ['1', '3', '4', '5'],
        'Resposta': '5',
    },
]
qtd_acertou = 0
for i in pergunta:
    print('Pergunta:', i['Pergunta'])
    print()
    opcoes = i['Opcões']
    for cont, opcao in enumerate(opcoes):
        cont = 1
        print(f'{i}),{opcao}')
    print()
    escolha = int(input('Escolha uma opção: '))

    acertou = False
    len_opcoes = len(opcoes)

    if escolha >= 0 and escolha <= len_opcoes:
        if opcoes[escolha] == i['Resposta']:
            acertou = True

    if acertou:
        qtd_acertou += 1
        print('Vocé acertou')
    else:
        print('Vocé não acertou')

print('Vocé acertou', qtd_acertou)
print('de', len(pergunta), 'perguntas')
