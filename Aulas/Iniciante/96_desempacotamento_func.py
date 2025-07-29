# Desempacomento em chamadas de metodos e funções

string = 'ABCD'
lista = ['Musarelo', 'Heleno', 1, 2, 3, 'Calabreso']
tupla = 'Python', 'é', 'legal'

# p, b, *_, ap, u = lista
# print(p, u, ap)

for nome in lista:
    print(nome)
    print(nome, end=' ')  # Isso é pra colocar na mesma linha
    # tem tambem sep=' '

# Tudo isso é igual a isso:
print(*lista)
print(*string)
print(*tupla)
