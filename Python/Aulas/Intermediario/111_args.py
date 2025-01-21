'''
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
'''

# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, *resto)


# def soma(x,y):
#    return x+y

def soma(*args):
    total = 0
    for num in args:
        total += num
        return total


numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

# *args = sem limite para o desempacotamento
# sun() = soma dos numeros em PYTHON


soma_1_2_3 = soma(*numeros)
print(soma_1_2_3)

print(sum((numeros)))

# print(sum((2,3,4)))
