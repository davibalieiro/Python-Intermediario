'''
Higher Order Function
Funções de Primeira classe

'''
# Tudo isso pra fazer uma coisa
# Ta passando por tudo pra fazer um negocio


def coisar(mesn, nome):
    return f'{mesn}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(coisar, 'Complicação de merda', 'Desgraça'))

print(executa(coisar, 'Complicação de merda', 'Desgraça'))

print(executa(coisar, 'Complicação de merda', 'Desgraça'))
