'''
Closre e funções que retoram outra funções
'''


def criar_ola(ola):
    def saudar(nome):
        return f'{ola}, {nome}'
    return saudar


s1 = criar_ola('ola',)
print(s1('Davi'))
