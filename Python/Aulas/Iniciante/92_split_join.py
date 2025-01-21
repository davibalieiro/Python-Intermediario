'''
split e join com list e srt
split = divide uma string
join = une uma string

'''
frase = 'Olha que coisa, mais interessante'
lista = frase.split(',')

for i, palavra in enumerate(lista):
    # strip = isso é para retirar os espaço do começo e do final
    print(lista[i].strip())


print(lista)
