'''
Sets - Conhuntos em Python (tipo set)
Conjuntos são ensinados na matematica
Sets em python são mutaveis, porem aceitam apenas tipos imutaveis como valor interno.

set(iteravél) ou set {1, 2, 3}

Sets são eficienes para remover valores duplados de iteraveis
 - else não tem índexes;
 - else não garatem ordem;
 - else sãoiteraveis (for, in, not in)

# set() - Vazio
 
Metodos uteis:
 - add
 - update
 - clear 
 - discard

Operadores uteis:
 - União | (union) - une
 - Interseção & (inersection) - itens presentes em ambos
 - diferença - itens presentes apenas no set da esquerda
 - diferença simetrica ^ - itens que estao em ambos 
 
'''
'''
l1 = [1, 2, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l1)
'''
'''
s1 = set()
s1.add('Davi')
s1.add(1)
s1.update('Hello')
#s1.clear()
s1.discard('Davi')
print(s1)
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2
print(s3)


# Exemplo de uso de stes

letras = set()
while True:
    letra = input('Digite uma letra:')
    letras.add(letra)

    if 'd' in letras:
        print('Parabens')
        break
    print(letras)
