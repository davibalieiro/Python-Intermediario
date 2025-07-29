palavra_secreta = 'Bahianinho'
acertos = ''
tentativas = 0
while True:
    letra = input('Digite uma letra: ')
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue
    if letra in palavra_secreta:
        acertos += letra

    palavra_formada = ''
    for letra_encontradas in palavra_formada:
        
        if letra_encontradas in acertos:
            palavra_formada += letra_encontradas
            
        else:
            palavra_formada += '*'

        print(palavra_formada)
