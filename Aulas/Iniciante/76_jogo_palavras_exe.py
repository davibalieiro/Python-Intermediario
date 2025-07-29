"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = 'abracadabra'
acertos = ''
tentou = 0
while True:

    letra = input('Digite uma letra: ')
    tentou += 1

    if len(letra) > 1:
        print('Digite apenas uma letra ')
        continue

    if letra in palavra:
        acertos += letra

    palavra_formar = ''
    for secreto in palavra:
        if secreto in acertos:
            palavra_formar += secreto

        else:
            palavra_formar += '*'

    print(palavra_formar)

    if palavra_formar == palavra:
        os.system('cls')
        print('PARABENS VOCÉ ACERTOU')
        print(f'Palavra formada: {palavra_formar}')
        print(f'Sua tentativa foram {tentou}')

        acertos = ''
        tentou = 0
