# # Variavel livre + nonLocal

# def fora(x):
#     a = 1

#     def dentro():
#         # print(locals())
#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)
# print(dentro1())
# print(dentro2())

def concatenar(inical):
    valor = inical

    def interna(concaterna):
        nonlocal valor
        valor += concaterna
        return valor
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
